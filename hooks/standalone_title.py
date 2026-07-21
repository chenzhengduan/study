import re


def on_post_page(output, page, config):
    standalone_title = page.meta.get("standalone_title") if page.meta else None
    if not standalone_title:
        return output

    return re.sub(
        r"<title>.*?</title>",
        f"<title>{standalone_title}</title>",
        output,
        count=1,
        flags=re.DOTALL,
    )
