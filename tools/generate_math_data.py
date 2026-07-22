from __future__ import annotations

import json
import random
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "math"
QUESTIONS_PATH = OUT_DIR / "questions.json"
INDEX_PATH = OUT_DIR / "index.json"

RANDOM_SEED = 20260722
TARGET_COUNT = 1024


@dataclass(frozen=True)
class Category:
    code: str
    name: str
    icon: str
    interaction_type: str
    maker: Callable[[random.Random, "Category", int, int], dict[str, Any]]


SCENES = [
    ("早餐桌", "蓝莓", "小碗"),
    ("客厅地毯", "积木", "小筐"),
    ("超市货架", "苹果", "购物袋"),
    ("公园长椅", "松果", "纸袋"),
    ("玩偶家", "小熊贴纸", "盒子"),
    ("厨房门口", "勺子", "杯子"),
    ("阳台花盆旁", "小石子", "托盘"),
    ("饭后收拾", "筷子", "抽屉"),
    ("电梯口", "楼层卡", "数字卡"),
    ("卧室书桌", "彩笔", "笔筒"),
    ("门口鞋架", "小鞋卡", "鞋盒"),
    ("散步路上", "树叶", "口袋"),
    ("拼图垫上", "方形纸片", "信封"),
    ("水果盘边", "橘子瓣", "盘子"),
    ("玩具车道", "小车", "停车位"),
    ("洗手台边", "毛巾夹", "篮子"),
]

PEOPLE = ["妈妈", "爸爸", "奶奶", "哥哥", "姐姐", "外婆"]
ANIMALS = ["小兔", "小猫", "小狗", "小熊", "小鸭", "小羊"]
CLASSIFY_OBJECTS = [
    ("彩色纽扣", ["红色", "黄色", "蓝色", "大号", "小号", "两孔", "四孔"]),
    ("积木", ["红色", "黄色", "绿色", "方形", "三角形", "长条形", "带圆点"]),
    ("图形卡片", ["圆形", "三角形", "正方形", "大号", "小号", "有花纹", "没有花纹"]),
    ("玩具动物卡", ["会飞的", "会游泳的", "住在农场的", "有四条腿的", "大动物", "小动物", "有翅膀的"]),
    ("袜子卡片", ["红色", "蓝色", "长袜", "短袜", "有条纹", "有圆点", "纯色"]),
]
ORDER_WORDS = ["最前面", "中间", "最后面", "左边", "右边", "第二个"]
SHAPES = ["正方形", "三角形", "长方形", "圆形纸片", "半圆纸片"]


def pick_scene(rng: random.Random, offset: int = 0) -> tuple[str, str, str]:
    return SCENES[(rng.randrange(len(SCENES)) + offset) % len(SCENES)]


def clamp_small(n: int) -> int:
    return max(-5, min(20, n))


def make_base(
    *,
    category: Category,
    difficulty: int,
    seq: int,
    scene: str,
    question: str,
    materials: list[str],
    parent_script: str,
    follow_ups: list[dict[str, str]],
    interaction: dict[str, Any],
    answer: str,
    explanation: str,
    possible_responses: list[str],
    observation_focus: list[str],
    avoid_saying: list[str],
    extension_questions: list[str],
    title: str,
) -> dict[str, Any]:
    return {
        "id": f"math-{category.code}-{difficulty}-{seq:03d}",
        "age_range": "4-7",
        "difficulty": difficulty,
        "category": category.name,
        "category_code": category.code,
        "icon": category.icon,
        "scene": scene,
        "title": title,
        "question": question,
        "materials": materials,
        "parent_script": parent_script,
        "follow_ups": follow_ups,
        "interaction": interaction,
        "answer": answer,
        "explanation": explanation,
        "possible_responses": possible_responses,
        "observation_focus": observation_focus,
        "avoid_saying": avoid_saying,
        "extension_questions": extension_questions,
    }


def common_parent(opening: str, item: str) -> str:
    return (
        f"{opening} 先让孩子用{item}摆一摆或画一画，再问："
        "“你是怎么想到的？还有别的方法吗？”不要急着评价对错。"
    )


def common_follow(item: str, change: str) -> list[dict[str, str]]:
    return [
        {
            "round": "第一轮追问",
            "prompt": f"“你为什么这样想？能用{item}摆出一种可能吗？”",
            "goal": "鼓励孩子说明理由，而不是只报一个数。",
        },
        {
            "round": "第二轮变化",
            "prompt": f"“如果{change}，你的想法还成立吗？”",
            "goal": "观察孩子能否在条件变化后重新判断。",
        },
    ]


def interaction(kind: str, **data: Any) -> dict[str, Any]:
    return {"type": kind, **data}


def make_insufficient(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, container = pick_scene(rng)
    animal = rng.choice(ANIMALS)
    total = rng.randint(7, 16)
    giver = rng.choice(PEOPLE)
    clue = rng.choice(["又添了一些", "拿走了一些后又补了一些", "和另一堆合在一起", "从别处拿来一些"])
    if difficulty <= 2:
        question = f"在{scene}，{animal}原来有一些{item}，{giver}{clue}，现在{container}里一共有{total}个。{animal}原来有几个{item}？"
    else:
        question = f"在{scene}，{animal}说自己现在有{total}个{item}，中间{giver}曾经{clue}。只听这些话，能确定一开始有几个吗？"
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="条件够不够",
        question=question,
        materials=[item, container, "数字卡"],
        parent_script=common_parent("把“原来、后来、现在”三个时间点慢慢说清楚。", item),
        follow_ups=common_follow(item, f"补充说{giver}后来给了{rng.randint(2, 6)}个{item}"),
        interaction=interaction("condition_check", choices=["能确定", "不能确定", "需要再问一个条件"], missing_info=["后来变化了多少"]),
        answer="不能确定，需要知道中间具体增加或减少了多少。补充条件后才可能算出一个确定结果。",
        explanation="现在的总数只是结果，原来的数量和中间变化量都可能不同。比如原来4个后来加6个，或原来7个后来加3个，都可能到同一个总数。",
        possible_responses=["直接说一个数", "说不知道", "提出要知道后来给了几个", "摆出两种不同可能"],
        observation_focus=["能否发现信息不足", "能否说出缺少的条件", "能否举出不同可能", "条件补充后能否更新判断"],
        avoid_saying=["这题没答案", "你怎么还不会减法", "答案就是某一个数"],
        extension_questions=[
            f"如果原来有{rng.randint(2, 6)}个，后来可能变化了多少？",
            "你能编一道让别人发现条件不够的问题吗？",
            "怎样加一句话，问题就能确定了？",
        ],
    )


def make_multiple(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, container = pick_scene(rng)
    parts = 2 if difficulty == 1 else 3
    total = rng.randint(8, 18)
    limit = rng.choice(["每份至少有1个", "有一份可以是0个", "不能每份一样多", "其中一份要比另一份多"])
    group_container = rng.choice(["小盘子", "小盒子", "纸圈", "小筐"])
    question = f"在{scene}，有{total}个{item}要放进{parts}个{group_container}。如果{limit}，可以怎么放？请至少想出两种办法。"
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="多种答案",
        question=question,
        materials=[item, group_container],
        parent_script=common_parent("告诉孩子这题可能不止一种答案。", item),
        follow_ups=common_follow(item, f"再加一个限制：有一个{group_container}里正好有{rng.randint(2, 5)}个"),
        interaction=interaction("arrange_groups", total=total, groups=parts, container=group_container, rule=limit, min_solutions=2),
        answer="可能有多种答案，只要总数和限制都满足即可。",
        explanation="这类问题重点不是最快算出一个答案，而是检查每一种摆法是否同时满足总数和限制。孩子可以先摆，再数，再换一种摆法。",
        possible_responses=["只给出一种分法", "试着交换两份的位置", "发现限制会排除某些分法", "自己提出新的限制"],
        observation_focus=["能否主动寻找第二种方法", "能否检查限制", "是否把位置交换误认为新思路", "能否解释为什么可行"],
        avoid_saying=["只有这个答案", "快点算", "你随便摆一个就行"],
        extension_questions=["如果要让方法变少，可以加什么限制？", "如果允许空盒子，会多出哪些可能？", "你能让另一个人也找出不同答案吗？"],
    )


def make_reverse(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    end = rng.randint(8, 18)
    delta = rng.randint(2, 7)
    start = end - delta
    action = rng.choice(["放进", "送来", "补上", "添了"])
    if difficulty >= 3:
        question = f"在{scene}，两堆{item}合起来是{end}个，其中一堆比另一堆多{delta if delta % 2 == 0 else delta + 1}个。两堆可能各是多少？"
        ans = "可以通过摆两堆并慢慢调整来找；如果差和总数能同时满足，就合理。"
    else:
        question = f"在{scene}，一个盒子后来被{action}{delta}个{item}，现在有{end}个。盒子原来有几个？你能倒着想吗？"
        ans = f"原来有{start}个。因为后来多了{delta}个，倒着想就是从{end}个里拿回{delta}个。"
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="反向思考",
        question=question,
        materials=[item, "小盒子", "数字卡"],
        parent_script=common_parent("请孩子先讲故事的顺序，再试着倒着讲一遍。", item),
        follow_ups=common_follow(item, f"把后来{action}的数量改成{rng.randint(1, 5)}个"),
        interaction=interaction("reverse_operation", end=end, change=delta, operation=action),
        answer=ans,
        explanation="反向问题让孩子从结果回到起点。可以用实物先做正向变化，再把动作倒回来，帮助孩子理解“撤回一个动作”。",
        possible_responses=["从头试一个数", "直接用减法", "把实物倒着拿回去", "能说出正向检查"],
        observation_focus=["能否理解变化方向", "能否用实物验证", "能否用自己的话说明倒着想", "是否只背算式"],
        avoid_saying=["这就是减法题", "你应该列式", "反过来算就完了"],
        extension_questions=["你能编一个从结果倒推的故事吗？", "如果后来不是增加而是拿走，倒着该怎么做？", "怎样检查你的答案？"],
    )


def make_counterexample(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    claims = [
        f"两堆{item}合起来，一定比每一堆都多。",
        f"{item}排得越长，数量一定越多。",
        f"大的{item}一定比小的{item}多。",
        f"先拿走再放回，最后一定变少。",
        f"看到数字大，就一定表示东西更多。",
    ]
    claim = claims[(seq + difficulty) % len(claims)]
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="寻找反例",
        question=f"在{scene}，{rng.choice(ANIMALS)}说：“{claim}”你觉得每次都对吗？能找一个不一样的例子吗？",
        materials=[item, "纸片", "数字卡"],
        parent_script=common_parent("先让孩子判断“是不是每次都这样”，再请孩子亲手造一个例子。", item),
        follow_ups=common_follow(item, "把其中一堆换成0个，或把同样数量摆得一疏一密"),
        interaction=interaction("find_counterexample", claim=claim, expected_action="make_or_draw_one_counterexample"),
        answer="不一定。只要能找到一个合理的不同情况，这句话就不是每次都成立。",
        explanation="反例意识的核心是区分“有时候对”和“每次都对”。家长可以让孩子先相信它，再用实物尝试推翻它。",
        possible_responses=["说看起来对", "摆出一个普通例子", "找到0或摆放疏密造成的反例", "改口说不一定"],
        observation_focus=["能否理解“一定”的含义", "能否主动找特殊情况", "能否接受原判断被改变", "能否说出反例为什么有效"],
        avoid_saying=["错了，当然不一定", "你被骗了", "这题是脑筋急转弯"],
        extension_questions=["还有别的反例吗？", "这句话什么时候是对的？", "怎样把这句话改得更准确？"],
    )


def make_invariant(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    a = rng.randint(4, 10)
    b = rng.randint(3, 9)
    shift = rng.randint(1, min(3, b))
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="保持不变",
        question=f"在{scene}，一边有{a}个{item}，另一边有{b}个{item}。如果从第二边挪{shift}个到第一边，总数会变吗？为什么？",
        materials=[item, "两张纸当作两边"],
        parent_script=common_parent("让孩子先摆出两边，再真的挪动，看每一边变了什么、总共变了什么。", item),
        follow_ups=common_follow(item, f"从第一边再挪{shift}个回第二边"),
        interaction=interaction("move_and_compare", left=a, right=b, move=shift),
        answer="总数不变。只是位置或分组变了，所有东西仍然都在这两边里。",
        explanation="一边增加多少，另一边就减少多少，合起来的总量没有丢也没有新增。重点是让孩子观察变化和不变同时存在。",
        possible_responses=["只关注某一边变多", "说总数也变多", "重新数全部", "说只是换了地方"],
        observation_focus=["能否区分部分和整体", "能否追踪移动过程", "能否说明什么变了什么没变", "能否迁移到新数量"],
        avoid_saying=["这叫加减抵消", "总数当然不变", "你不用数也应该知道"],
        extension_questions=["如果拿走后没有放到另一边，总数还不变吗？", "你能自己设计一个总数不变的动作吗？", "家里的杯子换位置，总杯数会变吗？"],
    )


def make_max_min(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    people = rng.randint(3, 5)
    total = rng.randint(people + 4, people + 13)
    at_least = 1 if difficulty <= 2 else rng.randint(1, 2)
    max_one = total - at_least * (people - 1)
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="最多与最少",
        question=f"在{scene}，{people}个小朋友分{total}个{item}，每个人至少有{at_least}个。想让其中一个小朋友拿得最多，他最多能拿几个？",
        materials=[item, "代表小朋友的纸片"],
        parent_script=common_parent("先保证每个人都有，再讨论怎样把剩下的尽量放给一个人。", item),
        follow_ups=common_follow(item, f"每个人至少要有{at_least + 1}个"),
        interaction=interaction("optimize_distribution", total=total, people=people, at_least=at_least, target="maximum_one_child"),
        answer=f"最多是{max_one}个。要先给其他{people - 1}个人各{at_least}个，剩下的都给目标小朋友。",
        explanation="这是在限制条件下找最多。不能只把全部给一个人，因为还要满足每个人至少有一些。",
        possible_responses=["把所有都给一个人", "平均分", "先照顾其他人再集中剩下的", "尝试不同摆法比较"],
        observation_focus=["能否同时记住总数和至少条件", "能否用极端摆法找最多", "能否检查每个人是否满足", "能否解释为什么不能再多"],
        avoid_saying=["你太贪心了", "这就是最大值", "直接用公式"],
        extension_questions=["如果想让一个人最少，他可以拿几个？", "怎样分看起来更公平？", "如果多来一个小朋友，答案会怎样变？"],
    )


def make_fair(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    people = rng.randint(2, 4)
    total = rng.randint(5, 17)
    can_equal = total % people == 0
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="公平与平均",
        question=f"在{scene}，{total}个{item}要分给{people}个小朋友，每个{item}不能掰开。能分得完全一样多吗？怎样才算公平？",
        materials=[item, "小盘子"],
        parent_script=common_parent("先让孩子说自己的公平标准，再摆给每个小朋友看。", item),
        follow_ups=common_follow(item, f"允许剩下1个先放在中间不分"),
        interaction=interaction("fair_share", total=total, people=people, indivisible=True),
        answer="能否完全一样多要看能不能每轮每人都分到一个且没有剩余；公平也可以讨论轮流、剩余暂存等办法。",
        explanation=f"这道题把数量和公平判断放在一起。当前数量{'可以' if can_equal else '不一定可以'}完全平均，但孩子可以提出“剩下的怎么办”的规则。",
        possible_responses=["平均摆放", "说剩下的给某个人", "提出轮流拿剩下的", "认为差1个也可以接受"],
        observation_focus=["能否一轮一轮分", "能否发现剩余", "能否表达公平标准", "能否接受公平不只有一种解释"],
        avoid_saying=["公平就是每人一样", "剩下的随便给谁", "你分错了"],
        extension_questions=["如果多一个或少一个，会不会更容易平均？", "如果东西可以切开，想法会变吗？", "你能设计一个大家都同意的规则吗？"],
    )


def make_order(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    roles = rng.sample(ANIMALS, 4)
    if difficulty <= 2:
        question = f"在{scene}，{roles[0]}排在{roles[1]}前面，{roles[2]}排在{roles[1]}后面。谁一定不在最后？谁可能在最前？"
    else:
        question = f"在{scene}，{roles[0]}不在第一个，{roles[1]}在{roles[2]}前面，{roles[3]}不在最后。它们可能怎样排？请摆出两种可能。"
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="顺序推理",
        question=question,
        materials=["动物卡片", item],
        parent_script=common_parent("把每个角色画成卡片，读一句条件就摆一次。", "动物卡片"),
        follow_ups=common_follow("动物卡片", f"再加一句：{roles[2]}不能站在{rng.choice(ORDER_WORDS)}"),
        interaction=interaction("order_cards", roles=roles, constraints="front_back_or_not_position"),
        answer="答案可能不唯一。所有摆法都必须同时满足每一句位置条件。",
        explanation="顺序推理适合用卡片试摆。孩子需要把每个条件保留下来，不能只记住最后一句。",
        possible_responses=["只按一句条件摆", "摆出一种后停止", "发现有多种排法", "用“不可能在某处”来排除"],
        observation_focus=["能否逐句检查条件", "能否理解前后左右", "能否保留多个限制", "能否找出不唯一的排法"],
        avoid_saying=["你记性不好", "唯一答案就是这个", "别摆了直接想"],
        extension_questions=["如果换成从右往左看，谁的位置会变？", "你能加一句让答案变成唯一吗？", "哪张卡片最容易确定？为什么？"],
    )


def make_truth(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    speaker = rng.choice(ANIMALS)
    claim = rng.choice([
        "看起来占地方多，数量就一定多",
        "两个盒子一样重，里面的东西数量就一样",
        "排在右边的数字一定更大",
        "先来的小朋友一定排在最前面",
        "每个人都多拿一个，总数就会变多",
    ])
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="真假判断",
        question=f"在{scene}，{speaker}说：“{claim}。”你同意吗？请用{item}或动作证明给家长看。",
        materials=[item, "两个盒子", "纸条"],
        parent_script=common_parent("请孩子先表态，再用一个例子支持或改变自己的判断。", item),
        follow_ups=common_follow(item, "换一种摆法或换一种盒子"),
        interaction=interaction("true_false_with_reason", claim=claim, choices=["同意", "不同意", "有时候同意"]),
        answer="多数这类说法不是永远正确，需要看具体条件。孩子能说出“什么时候对、什么时候不对”就是好答案。",
        explanation="真假判断不是为了抓错，而是让孩子练习用例子解释判断。家长应关注理由是否和事实一致。",
        possible_responses=["只说对或不对", "用一个例子说明", "发现“有时候”", "提出还要看具体情况"],
        observation_focus=["能否给出理由", "能否用实物支持判断", "能否区分绝对话和有条件的话", "能否修正表达"],
        avoid_saying=["你猜错了", "这句话当然不严谨", "我告诉你标准答案"],
        extension_questions=["怎样说会更准确？", "你能找一个支持它的例子吗？", "你能找一个反对它的例子吗？"],
    )


def make_pattern(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    start = rng.randint(1, 4)
    step = rng.randint(1, 3)
    pattern = [start + i * step for i in range(4)]
    if difficulty >= 3 and seq % 2 == 0:
        pattern = [1, 2, 4, 7]
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="规律变化",
        question=f"在{scene}，家长摆出每组{item}数量：{pattern[0]}、{pattern[1]}、{pattern[2]}、{pattern[3]}。后面可能是多少？你能说出理由，或想出另一种规律吗？",
        materials=[item, "纸条", "数字卡"],
        parent_script=common_parent("不要只问下一个数，重点追问孩子看到的变化。", item),
        follow_ups=common_follow(item, "从后往前看，或者把第一个数换掉"),
        interaction=interaction("pattern_continue", sequence=pattern, accepts_multiple_rules=True),
        answer="只要规律解释清楚并能继续生成，就可以是合理答案；有些序列可能有不止一种续法。",
        explanation="规律题的目标是让孩子表达“为什么这样接”。家长可以把孩子的规则再用下一项检查一次。",
        possible_responses=["直接猜下一个", "说每次多几个", "提出颜色或形状规律", "发现可以有另一种解释"],
        observation_focus=["能否说出变化关系", "能否验证下一项", "能否接受多种规律", "能否自己改规则"],
        avoid_saying=["下一个只可能是这个", "你猜中了就行", "不用解释"],
        extension_questions=["如果从后往前看，规律怎么说？", "你能摆一个有两种解释的规律吗？", "如果跳过一个，中间可能是什么？"],
    )


def make_create(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    target = rng.randint(6, 16)
    requirement = rng.choice(["没有唯一答案", "需要别人补一个条件", "可以用实物摆出来", "能让别人解释为什么"])
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="自己出题",
        question=f"在{scene}，答案先定为{target}。你能用{item}编一道数学问题吗？这道题最好{requirement}。",
        materials=[item, "白纸", "数字卡"],
        parent_script=common_parent("让孩子先讲故事，再请家长当孩子的学生来回答。", item),
        follow_ups=common_follow(item, f"把答案改成{target + rng.randint(1, 3)}，但故事场景不变"),
        interaction=interaction("child_create_problem", target_answer=target, requirement=requirement),
        answer="孩子编出的题只要情境清楚、条件和答案能对应，就是合理作品；开放要求下可以不止一个答案。",
        explanation="自己出题能检查孩子是否理解数量关系，也能训练表达。家长要帮助孩子把缺少的条件说清，而不是替孩子重写题目。",
        possible_responses=["编普通加法故事", "编减法故事", "漏掉关键条件", "创造一个开放问题"],
        observation_focus=["能否把答案和故事对应", "能否说清条件", "能否接受别人追问", "能否改进自己的题"],
        avoid_saying=["你编得不像题", "这题太简单", "我来替你编"],
        extension_questions=["你能让这题有两种答案吗？", "你能让别人必须问一个问题才会做吗？", "你能把它改成找反例的问题吗？"],
    )


def make_proof(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    total = rng.randint(8, 16)
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="简单说明为什么",
        question=f"在{scene}，{total}个{item}被分成两堆。不管一堆多一点还是少一点，两堆合起来为什么还是{total}个？你能摆、画或讲给家长听吗？",
        materials=[item, "两张纸", "笔"],
        parent_script=common_parent("请孩子先做几种分法，再找共同点。", item),
        follow_ups=common_follow(item, "把两堆改成三堆"),
        interaction=interaction("explain_with_objects", total=total, representations=["摆", "画", "说"]),
        answer=f"因为没有新增或拿走{item}，只是分堆方式变了，所以合起来仍然是{total}个。",
        explanation="这不是正式证明，而是让孩子用自己的语言说明“不变”的理由。多个例子能帮助孩子从具体摆法看到共同关系。",
        possible_responses=["重新数每一种分法", "说都在这里", "只记住一个例子", "能总结没有多也没有少"],
        observation_focus=["能否从例子走向一般说明", "能否用图或实物解释", "能否说清没有新增或减少", "能否迁移到三堆"],
        avoid_saying=["这叫守恒", "你证明一下", "背下来就行"],
        extension_questions=["如果偷偷拿走1个，还成立吗？", "换成三堆为什么也可以？", "你能找一个总数会改变的动作吗？"],
    )


def make_space(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, _, _ = pick_scene(rng)
    shape = rng.choice(SHAPES)
    count = rng.randint(3, 6)
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="空间与形状",
        question=f"在{scene}，用{count}块一样的{shape}可以拼出哪些不一样的形状？旋转一下还算不算新的？你为什么这样想？",
        materials=[shape, "纸片", "桌面"],
        parent_script=common_parent("先让孩子自由拼，再一起比较哪些只是转了方向，哪些真的不一样。", shape),
        follow_ups=common_follow(shape, f"少用1块或多用1块{shape}"),
        interaction=interaction("shape_build", shape=shape, count=count, compare_rotation=True),
        answer="可以有多种拼法。是否把旋转后的形状算新形状，需要先说清比较规则。",
        explanation="空间题重点是比较、旋转和规则约定。家长可让孩子把形状描边，再转一转看是否能重合。",
        possible_responses=["拼出一条长条", "拼出拐弯形", "把旋转当成新形状", "提出自己的比较规则"],
        observation_focus=["能否尝试多种拼法", "能否理解旋转后可能相同", "能否说出比较规则", "手眼协调与空间想象"],
        avoid_saying=["这不是标准图形", "只有课本上那种才对", "别乱拼"],
        extension_questions=["如果翻过来能重合，还算一样吗？", "怎样拼最像楼梯？", "你能让别人照你的话拼出来吗？"],
    )


def make_estimate(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, container = pick_scene(rng)
    actual = rng.randint(9, 35)
    choices = sorted({max(1, actual - rng.randint(4, 9)), actual, actual + rng.randint(4, 12)})
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="估计与验证",
        question=f"在{scene}，{container}里有一把{item}。不马上数，你觉得更接近{choices[0]}个、{choices[1]}个，还是{choices[2]}个？先说理由，再数一数验证。",
        materials=[item, container],
        parent_script=common_parent("先盖住一部分或快速看一眼，让孩子说估计理由，再一起数。", item),
        follow_ups=common_follow(item, f"把{container}里的{item}分成两小堆再估"),
        interaction=interaction("estimate_then_count", choices=choices, actual=actual, hide_actual_until_count=True),
        answer=f"实际准备时可放{actual}个左右。好答案应包含估计理由，验证后比较差多少。",
        explanation="估计不是瞎猜。孩子可以根据一小堆有多少、容器大小、疏密程度来判断，再用计数修正感觉。",
        possible_responses=["随便选一个", "根据满不满来猜", "先数一小撮再推想", "验证后调整下次估计"],
        observation_focus=["能否说估计依据", "能否接受估计有误差", "能否用部分推整体", "能否比较估计和实际"],
        avoid_saying=["猜错了", "这有什么好估的", "必须正好猜中"],
        extension_questions=["如果换大一点的容器，看起来会变多吗？", "你能先估一半再估全部吗？", "下次怎样猜得更接近？"],
    )


def make_negative(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene = rng.choice(["电梯口", "地下停车场入口", "温度计旁", "楼梯间"])
    start = rng.randint(-2, 5)
    # 控制结果不低于 -5，难度来自方向变化，而不是过大的负数。
    move = rng.randint(1, max(2, min(5, start + 5)))
    if "温度" in scene:
        question = f"{scene}，早上是{start}度，晚上降了{move}度。晚上可能是多少度？可以用温度卡往下走一走。"
        answer = f"晚上是{start - move}度。重点是理解从{start}继续往下数{move}步。"
        material = "温度卡"
    else:
        question = f"{scene}，电梯现在在{start}楼，向下走{move}层，会到哪里？如果经过0下面，怎么表示？"
        answer = f"会到{start - move}楼。可以把地上、地下或0上下用卡片排出来再走。"
        material = "楼层卡"
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="简单负数思维",
        question=question,
        materials=[material, "小玩偶"],
        parent_script=common_parent("把楼层或温度排成一条线，让孩子拿玩偶一步一步移动。", material),
        follow_ups=common_follow(material, f"先向上走{rng.randint(1, 3)}步，再向下走{rng.randint(2, 5)}步"),
        interaction=interaction("number_line_walk", start=start, move=-move, context=scene),
        answer=answer,
        explanation="负数先作为方向和位置理解即可，不需要讲复杂规则。向下、变冷、欠缺都可以用一条线表示。",
        possible_responses=["停在0不敢继续", "用地下1层表示-1", "一步一步数到答案", "能解释上和下的方向"],
        observation_focus=["能否理解0下面还有位置", "能否按方向移动", "能否把负数和生活场景联系", "是否被符号吓住"],
        avoid_saying=["这是负数运算", "记住负负得正", "你必须写成算式"],
        extension_questions=["如果再向上走几层会回到0？", "温度从-1升高2度在哪里？", "你能自己画一条楼层线吗？"],
    )


def make_classify(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, _, _ = pick_scene(rng)
    item, available_attrs = rng.choice(CLASSIFY_OBJECTS)
    attrs = rng.sample(available_attrs, 4)
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="分类与比较",
        question=f"在{scene}，混着一些{item}，它们的特点有：{attrs[0]}、{attrs[1]}、{attrs[2]}和{attrs[3]}。你能想出两种不同的分类方法吗？哪一种更方便找东西？",
        materials=[item, "小盒子", "标签纸"],
        parent_script=common_parent("先让孩子自己定分类规则，再请她解释为什么这样分。", item),
        follow_ups=common_follow(item, "同一个东西同时符合两个规则"),
        interaction=interaction("sort_objects", attributes=attrs, min_rules=2),
        answer="可以按颜色、形状、大小、用途、是否成对等分类。规则清楚且每个物品知道放哪里即可。",
        explanation="分类题培养孩子建立规则和比较规则。重点不是分得像成人，而是能说清自己的标准。",
        possible_responses=["只按颜色分", "改按大小分", "发现一个物品难放", "提出可以放到两个组"],
        observation_focus=["能否提出明确规则", "能否切换分类标准", "能否处理边界情况", "能否比较哪种规则更有用"],
        avoid_saying=["你分得不对", "只能按颜色", "别想那么多"],
        extension_questions=["如果只能用两个盒子怎么分？", "哪个规则会让每盒数量最接近？", "你能给家长出一个分类规则吗？"],
    )


def make_possibility(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, container = pick_scene(rng)
    colors = rng.sample(["红", "黄", "蓝", "绿", "白"], 3)
    known = rng.randint(2, 5)
    total = known + rng.randint(3, 8)
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="可能性判断",
        question=f"在{scene}，{container}中有{total}个{item}，已经看见{known}个是{colors[0]}色。闭眼摸一个，一定会摸到{colors[0]}色吗？可能摸到什么？",
        materials=[item, container, "布巾"],
        parent_script=common_parent("先区分“一定、可能、不可能”，再让孩子补充还需要知道什么。", item),
        follow_ups=common_follow(item, f"告诉孩子剩下的全是{colors[1]}色"),
        interaction=interaction("possibility_judgment", total=total, known_color={colors[0]: known}, terms=["一定", "可能", "不可能"]),
        answer="不能说一定。只看见一部分时，剩下的颜色还不知道，所以只能说可能摸到已知颜色，也可能有其他颜色。",
        explanation="可能性题帮助孩子处理不完整信息。家长应鼓励孩子说“我还需要知道盒子里其他是什么”。",
        possible_responses=["说一定是看见的颜色", "说不知道", "提出要看看剩下的", "用可能/不可能来表达"],
        observation_focus=["能否区分一定和可能", "能否意识到看见的不等于全部", "能否提出补充信息", "能否在新信息下改变判断"],
        avoid_saying=["你运气不好就错了", "概率就是几分之几", "猜一个颜色"],
        extension_questions=["如果全是同一种颜色，还叫可能吗？", "怎样放东西才能一定摸到红色？", "怎样放东西让蓝色不可能被摸到？"],
    )


def make_missing_part(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    total = rng.randint(8, 18)
    shown = rng.randint(2, total - 2)
    hidden = total - shown
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="看见与藏起",
        question=f"在{scene}，一共有{total}个{item}，桌上看得见{shown}个，剩下的被盖住了。盖住了几个？你能不用一直从1数到{total}吗？",
        materials=[item, "小布巾", "数字卡"],
        parent_script=common_parent("先让孩子用盖住动作理解整体和部分，再请她说自己的方法。", item),
        follow_ups=common_follow(item, f"改成看见{rng.randint(1, total - 1)}个"),
        interaction=interaction("part_whole_hidden", total=total, visible=shown),
        answer=f"盖住了{hidden}个。可以从看见的{shown}个往上数到{total}，也可以把整体拆成看见和盖住两部分。",
        explanation="这是整体和部分关系，不是单纯口算。家长可以让孩子先摆整体，再遮住一部分，最后用不同方法检查。",
        possible_responses=["从1重新数", "从看见的数接着数", "用拆分说出隐藏数量", "用实物打开检查"],
        observation_focus=["能否理解整体包含看见和藏起", "能否从中间接着数", "能否用实物验证", "能否说出不同方法"],
        avoid_saying=["这就是减法", "不要用手", "你算慢了"],
        extension_questions=["如果只知道藏起几个，能知道看见几个吗？", "你能让家长猜猜你藏了几个吗？", "怎样藏会让别人更难猜？"],
    )


def make_map_path(rng: random.Random, cat: Category, difficulty: int, seq: int) -> dict[str, Any]:
    scene, item, _ = pick_scene(rng)
    steps = rng.randint(2, 5)
    turns = rng.choice(["向左转", "向右转", "往前走", "退回一步"])
    return make_base(
        category=cat,
        difficulty=difficulty,
        seq=seq,
        scene=scene,
        title="路线与方向",
        question=f"在{scene}，把{item}当作小路。小玩偶先往前走{steps}步，再{turns}。它现在可能在哪里？如果从终点倒着走，能回到起点吗？",
        materials=[item, "小玩偶", "方向箭头卡"],
        parent_script=common_parent("在桌上摆出小路和箭头，让孩子边走边说方向。", item),
        follow_ups=common_follow(item, "把第二步换成相反方向"),
        interaction=interaction("path_walk", forward_steps=steps, turn=turns, reversible=True),
        answer="按路线摆法不同，终点可能不同；只要每一步方向清楚，就能倒着走回起点。",
        explanation="路线题训练空间方位和逆向操作。家长要先约定面朝哪边，再讨论左、右、前、后。",
        possible_responses=["左右混淆", "用手转动玩偶再判断", "发现倒着走要反过来做", "自己画路线"],
        observation_focus=["能否保持方向参照", "能否按步骤执行", "能否倒推路线", "能否用语言描述位置"],
        avoid_saying=["你左右都分不清", "看屏幕点就行", "不用摆"],
        extension_questions=["如果面朝相反方向，左边还是同一边吗？", "你能设计一条路线让家长走吗？", "怎样用最少步走回起点？"],
    )


CATEGORIES: list[Category] = [
    Category("condition", "条件不足", "❓", "condition_check", make_insufficient),
    Category("multi_answer", "多种答案", "🔀", "arrange_groups", make_multiple),
    Category("reverse", "反向问题", "↩️", "reverse_operation", make_reverse),
    Category("counterexample", "找反例", "🔍", "find_counterexample", make_counterexample),
    Category("invariant", "保持不变", "⚖️", "move_and_compare", make_invariant),
    Category("max_min", "最多与最少", "📈", "optimize_distribution", make_max_min),
    Category("fair_share", "公平与平均", "🤝", "fair_share", make_fair),
    Category("order", "顺序推理", "🚶", "order_cards", make_order),
    Category("truth", "真假判断", "✅", "true_false_with_reason", make_truth),
    Category("pattern", "规律变化", "🧩", "pattern_continue", make_pattern),
    Category("create", "自己出题", "✏️", "child_create_problem", make_create),
    Category("proof", "简单证明", "💬", "explain_with_objects", make_proof),
    Category("space", "空间与形状", "⬜", "shape_build", make_space),
    Category("estimate", "估计与判断", "👀", "estimate_then_count", make_estimate),
    Category("negative", "简单负数思维", "🏢", "number_line_walk", make_negative),
    Category("classify", "分类与比较", "🏷️", "sort_objects", make_classify),
    Category("possibility", "可能性判断", "🎲", "possibility_judgment", make_possibility),
    Category("part_whole", "整体与部分", "🫙", "part_whole_hidden", make_missing_part),
    Category("path", "路线与方向", "🧭", "path_walk", make_map_path),
]


REQUIRED_FIELDS = [
    "id",
    "age_range",
    "difficulty",
    "category",
    "category_code",
    "icon",
    "scene",
    "title",
    "question",
    "materials",
    "parent_script",
    "follow_ups",
    "interaction",
    "answer",
    "explanation",
    "possible_responses",
    "observation_focus",
    "avoid_saying",
    "extension_questions",
]


def has_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, list):
        return not value or any(has_empty(v) for v in value)
    if isinstance(value, dict):
        return not value or any(has_empty(v) for v in value.values())
    return False


def validate(questions: list[dict[str, Any]]) -> None:
    errors: list[str] = []
    if len(questions) < 1000:
        errors.append(f"题目数量不足: {len(questions)}")

    ids = [q.get("id", "") for q in questions]
    duplicate_ids = [item for item, count in Counter(ids).items() if count > 1]
    if duplicate_ids:
        errors.append(f"重复id: {duplicate_ids[:5]}")

    stems = [q.get("question", "") for q in questions]
    duplicate_stems = [item for item, count in Counter(stems).items() if count > 1]
    if duplicate_stems:
        errors.append(f"重复题干: {duplicate_stems[:3]}")

    categories = Counter(q["category"] for q in questions)
    if len(categories) < 15:
        errors.append(f"分类不足15类: {len(categories)}")

    difficulties = Counter(q["difficulty"] for q in questions)
    if set(difficulties) != {1, 2, 3, 4}:
        errors.append(f"难度未覆盖1-4级: {dict(difficulties)}")

    arithmetic_only = re.compile(r"^\s*\d+\s*[+\-]\s*\d+\s*(等于|=|是多少)")

    for index, question in enumerate(questions):
        missing = [field for field in REQUIRED_FIELDS if field not in question or has_empty(question[field])]
        if missing:
            errors.append(f"{question.get('id', index)} 空字段: {missing}")
            continue
        if question["age_range"] != "4-7":
            errors.append(f"{question['id']} age_range错误")
        if len(question["follow_ups"]) < 2:
            errors.append(f"{question['id']} 追问少于2轮")
        if not any("为什么" in str(follow) or "理由" in str(follow) for follow in question["follow_ups"]):
            errors.append(f"{question['id']} 缺少为什么/理由追问")
        if arithmetic_only.search(question["question"]):
            errors.append(f"{question['id']} 疑似纯口算题")
        if question["interaction"].get("type") == "":
            errors.append(f"{question['id']} interaction.type为空")

    if errors:
        sample = "\n".join(errors[:20])
        raise ValueError(f"题库校验失败，共{len(errors)}项:\n{sample}")


def build_questions() -> list[dict[str, Any]]:
    rng = random.Random(RANDOM_SEED)
    questions: list[dict[str, Any]] = []
    seen_questions: set[str] = set()
    seq_by_category_difficulty: Counter[tuple[str, int]] = Counter()

    while len(questions) < TARGET_COUNT:
        cat = CATEGORIES[len(questions) % len(CATEGORIES)]
        difficulty = (len(questions) // len(CATEGORIES)) % 4 + 1
        key = (cat.code, difficulty)
        seq_by_category_difficulty[key] += 1
        seq = seq_by_category_difficulty[key]
        for attempt in range(50):
            q_rng = random.Random(f"{RANDOM_SEED}:{cat.code}:{difficulty}:{seq}:{attempt}:{rng.random()}")
            question = cat.maker(q_rng, cat, difficulty, seq)
            if question["question"] not in seen_questions:
                seen_questions.add(question["question"])
                questions.append(question)
                break
        else:
            raise RuntimeError(f"无法为 {cat.code} 难度{difficulty} 序号{seq} 生成唯一题干")

    validate(questions)
    return questions


def build_index(questions: list[dict[str, Any]]) -> dict[str, Any]:
    by_category = Counter(q["category"] for q in questions)
    by_difficulty = Counter(str(q["difficulty"]) for q in questions)
    by_interaction = Counter(q["interaction"]["type"] for q in questions)
    return {
        "title": "4-7岁亲子数学思维题库",
        "generated_by": "tools/generate_math_data.py",
        "seed": RANDOM_SEED,
        "total": len(questions),
        "age_range": "4-7",
        "category_count": len(by_category),
        "difficulty_count": len(by_difficulty),
        "categories": [
            {
                "code": next(q["category_code"] for q in questions if q["category"] == category),
                "name": category,
                "icon": next(q["icon"] for q in questions if q["category"] == category),
                "count": count,
            }
            for category, count in sorted(by_category.items())
        ],
        "difficulties": dict(sorted(by_difficulty.items())),
        "interaction_types": dict(sorted(by_interaction.items())),
        "quality_checks": {
            "required_fields": REQUIRED_FIELDS,
            "min_questions": 1000,
            "duplicate_ids": 0,
            "duplicate_questions": 0,
            "min_follow_up_rounds": 2,
            "rejects_empty_fields": True,
            "rejects_arithmetic_only_stems": True,
        },
    }


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    questions = build_questions()
    index = build_index(questions)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    QUESTIONS_PATH.write_text(json.dumps(questions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(index, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
