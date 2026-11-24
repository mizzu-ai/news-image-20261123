import os
from PIL import Image, ImageDraw, ImageFont

def create_newspaper():
    width, height = 1024, 1024
    img = Image.new("RGB", (width, height), color="#FBF8F3")
    draw = ImageDraw.Draw(img)

    # Load fonts (fallback to default if specific ttf not found)
    def get_font(size, bold=False):
        font_paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ]
        for path in font_paths:
            if os.path.exists(path):
                try:
                    return ImageFont.truetype(path, size)
                except Exception:
                    continue
        return ImageFont.load_default()

    font_title = get_font(44, bold=True)
    font_subtitle = get_font(14, bold=False)
    font_section = get_font(12, bold=True)
    
    font_lead_head = get_font(24, bold=True)
    font_lead_body = get_font(13, bold=False)
    
    font_head = get_font(15, bold=True)
    font_body = get_font(11, bold=False)

    # Outer border
    draw.rectangle([15, 15, width - 15, height - 15], outline="#1A1A1A", width=3)
    draw.rectangle([19, 19, width - 19, height - 19], outline="#1A1A1A", width=1)

    # Header Section
    draw.text((width // 2, 32), "THE GLOBAL CHRONICLE", fill="#111111", font=font_title, anchor="mm")
    draw.line([30, 85, width - 30, 85], fill="#111111", width=2)
    
    date_str = "MONDAY, 23 NOVEMBER 2026  |  INTERNATIONAL EDITION  |  FIVE CENTS"
    draw.text((width // 2, 98), date_str, fill="#333333", font=font_subtitle, anchor="mm")
    draw.line([30, 115, width - 30, 115], fill="#111111", width=1)

    # Helper for text wrapping
    def wrap_text(text, font, max_width):
        words = text.split()
        lines = []
        current_line = []
        for word in words:
            test_line = " ".join(current_line + [word])
            bbox = font.getbbox(test_line)
            w = bbox[2] - bbox[0]
            if w <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
        if current_line:
            lines.append(" ".join(current_line))
        return lines

    # --- LEAD STORY: COP31 CLIMATE TALKS COLLAPSE ---
    lead_box = [30, 130, width - 30, 395]
    draw.rectangle(lead_box, outline="#444444", width=1, fill="#FFFFFF")
    draw.rectangle([35, 135, width - 35, 155], fill="#1A1A1A")
    draw.text((45, 138), "SPECIAL REPORT: UN CLIMATE SUMMIT COLLAPSE", fill="#FFFFFF", font=font_section)

    lead_title = "COP31 CLIMATE TALKS COLLAPSE IN ANTALYA AFTER RECORD 49-HOUR OVERRUN"
    y = 165
    for line in wrap_text(lead_title, font_lead_head, width - 80):
        draw.text((45, y), line, fill="#111111", font=font_lead_head)
        y += 28

    y += 5
    lead_text = (
        "The UN climate summit in Antalya, Turkey ended on Monday, 23 November 2026 without a deal "
        "following an unprecedented ~49-hour overrun. The European Union and over 130 nations firmly refused "
        "a final text that omitted any call to transition away from fossil fuels. The anticipated 'Antalya Pact' "
        "was not adopted, making it the longest and most contentious climate summit in UN history."
    )
    for line in wrap_text(lead_text, font_lead_body, width - 80):
        draw.text((45, y), line, fill="#222222", font=font_lead_body)
        y += 18

    # --- TWO COLUMN LAYOUT FOR STORIES 2 & 3 ---
    col_y = 410
    col_w = 468
    
    # Story 2: Ukraine Warship
    box2 = [30, col_y, 30 + col_w, col_y + 270]
    draw.rectangle(box2, outline="#444444", width=1, fill="#FFFFFF")
    draw.rectangle([35, col_y + 5, 30 + col_w - 5, col_y + 25], fill="#2C2C2C")
    draw.text((45, col_y + 7), "CONFLICT: NAVAL WARFARE", fill="#FFFFFF", font=font_section)
    
    y = col_y + 35
    h2 = "Ukraine Says It Sank Russian Warship Off Libya"
    for line in wrap_text(h2, font_head, col_w - 20):
        draw.text((45, y), line, fill="#111111", font=font_head)
        y += 20
    
    y += 5
    b2 = (
        "Kyiv announced on 23 Nov that its naval drones successfully sank the Russian corvette Merkury "
        "near the Libyan port of Benghazi. President Zelenskyy praised the operation. Meanwhile, NATO held "
        "an emergency meeting over Russian objects downing in Poland."
    )
    for line in wrap_text(b2, font_body, col_w - 20):
        draw.text((45, y), line, fill="#222222", font=font_body)
        y += 16

    # Story 3: Iran-US Hormuz Escalation
    col2_x = 526
    box3 = [col2_x, col_y, col2_x + col_w, col_y + 270]
    draw.rectangle(box3, outline="#444444", width=1, fill="#FFFFFF")
    draw.rectangle([col2_x + 5, col_y + 5, col2_x + col_w - 5, col_y + 25], fill="#2C2C2C")
    draw.text((col2_x + 15, col_y + 7), "GEOPOLITICS: STRAIT OF HORMUZ", fill="#FFFFFF", font=font_section)
    
    y = col_y + 35
    h3 = "Iran-US Escalation: Mines Hit Tankers & New US Sanctions"
    for line in wrap_text(h3, font_head, col_w - 20):
        draw.text((col2_x + 15, y), line, fill="#111111", font=font_head)
        y += 20
        
    y += 5
    b3 = (
        "Iran's Revolutionary Guards reported naval mines struck tankers attempting to cross the Strait of Hormuz. "
        "In response, the US Treasury imposed sweeping sanctions on 20+ exchange houses and front companies in Iran's shadow "
        "banking network on 23 November, amid heightened missile and drone activity."
    )
    for line in wrap_text(b3, font_body, col_w - 20):
        draw.text((col2_x + 15, y), line, fill="#222222", font=font_body)
        y += 16

    # --- TWO COLUMN LAYOUT FOR STORIES 4 & 5 ---
    bot_y = 695
    
    # Story 4: Indonesia Factory Fire
    box4 = [30, bot_y, 30 + col_w, bot_y + 295]
    draw.rectangle(box4, outline="#444444", width=1, fill="#FFFFFF")
    draw.rectangle([35, bot_y + 5, 30 + col_w - 5, bot_y + 25], fill="#2C2C2C")
    draw.text((45, bot_y + 7), "DISASTER: INDONESIA", fill="#FFFFFF", font=font_section)
    
    y = bot_y + 35
    h4 = "Indonesia Factory Fire Death Toll Rises to 24 in Cikande"
    for line in wrap_text(h4, font_head, col_w - 20):
        draw.text((45, y), line, fill="#111111", font=font_head)
        y += 20
        
    y += 5
    b4 = (
        "Authorities in Indonesia confirmed on Monday, 23 Nov 2026, that 24 people died in the devastating fire "
        "at the Fonusa Agung Mulia candy factory in Cikande, Banten. Emergency services and rescuers continue searching "
        "for dozens of workers still reported missing following the disaster."
    )
    for line in wrap_text(b4, font_body, col_w - 20):
        draw.text((45, y), line, fill="#222222", font=font_body)
        y += 16

    # Story 5: US Blacklists Megaspeed & Nvidia/Crypto
    box5 = [col2_x, bot_y, col2_x + col_w, bot_y + 295]
    draw.rectangle(box5, outline="#444444", width=1, fill="#FFFFFF")
    draw.rectangle([col2_x + 5, bot_y + 5, col2_x + col_w - 5, bot_y + 25], fill="#2C2C2C")
    draw.text((col2_x + 15, bot_y + 7), "MARKETS & TRADE: US BLACKLISTS MEGASPEED", fill="#FFFFFF", font=font_section)
    
    y = bot_y + 35
    h5 = "US Blacklists Megaspeed Over Nvidia Chip Diversion"
    for line in wrap_text(h5, font_head, col_w - 20):
        draw.text((col2_x + 15, y), line, fill="#111111", font=font_head)
        y += 20
        
    y += 5
    b5 = (
        "On 23 Nov 2026, the US Commerce Dept placed Singapore-based Megaspeed on its Entity List over suspected "
        "diversion of Nvidia AI chips to China. Nvidia fell ~23% in its worst week since 2008. Bitcoin dropped to ~$55,100 "
        "before recovering to around $61,000."
    )
    for line in wrap_text(b5, font_body, col_w - 20):
        draw.text((col2_x + 15, y), line, fill="#222222", font=font_body)
        y += 16

    # Save image
    img.save("entry.png", "PNG")
    print("Generated entry.png successfully (1024x1024).")

if __name__ == "__main__":
    create_newspaper()
