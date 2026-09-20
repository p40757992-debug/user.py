#!/usr/bin/env python3
import sys
import os
import asyncio  # <--- ဒါလေး ထည့်ပါ

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    import Phyo_User
    
    print("✅ Phyo_User ကို အောင်မြင်စွာ ခေါ်လိုက်ပါပြီ။ Program စတင်နေပါပြီ...\n")
    
    if hasattr(Phyo_User, 'main'):
        # async function ဖြစ်နေရင် asyncio.run နဲ့ ခေါ်ပါ
        asyncio.run(Phyo_User.main())
    elif hasattr(Phyo_User, 'show_menu'):
        Phyo_User.show_menu()
    else:
        print("⚠️ main() သို့မဟုတ် show_menu() function မတွေ့ပါ။")

except Exception as e:
    print(f"❌ Error တက်နေပါတယ်: {e}")