import os
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:4399"
OUT = os.path.expanduser("~/.hermes/wiki/blog_個人網站/output/verify_shots")
os.makedirs(OUT, exist_ok=True)

errors = []

with sync_playwright() as p:
    b = p.chromium.launch()

    ctx = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
    pg.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)

    pg.goto(BASE + "/", wait_until="networkidle")
    pg.screenshot(path=f"{OUT}/01_home_desktop.png", full_page=True)
    print("home title:", pg.title())
    print("home post items:", pg.locator(".post-item").count())

    # 深色模式切換（真實點擊，非直接改屬性）
    pg.click("#theme-toggle")
    pg.wait_for_timeout(200)
    theme = pg.evaluate("document.documentElement.getAttribute('data-theme')")
    print("theme after click:", theme)
    pg.screenshot(path=f"{OUT}/02_home_dark.png", full_page=True)

    pg.goto(BASE + "/posts/ddic-basics/", wait_until="networkidle")
    pg.click("#theme-toggle")
    pg.wait_for_timeout(200)
    pg.screenshot(path=f"{OUT}/03_article_dark.png", full_page=True)
    print("article h1:", pg.locator("h1").inner_text())
    print("article tables:", pg.locator(".prose table").count())
    ctx.close()

    ctx2 = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=3, is_mobile=True)
    pg2 = ctx2.new_page()
    pg2.goto(BASE + "/", wait_until="networkidle")
    pg2.screenshot(path=f"{OUT}/04_home_mobile.png", full_page=True)
    ctx2.close()

    b.close()

for f in sorted(os.listdir(OUT)):
    print("SHOT", f, os.path.getsize(os.path.join(OUT, f)), "bytes")
print("JS ERRORS:", errors if errors else "none")
