"""
Gabriel Website V4 Batch Update Script
Version: 1120v2
Date: 2025-11-20

This script updates all remaining pages with v4 header/footer templates.
"""

import re
from pathlib import Path

# Paths
V4_DIR = Path(r"C:\Users\Darry\ROOT_BODY\Organs\Gabriel_Website_v4")

# V4 Header Template (lines 47-98 from index.html)
V4_HEADER = '''<body class="bg-background-light dark:bg-background-dark font-display text-[#101622] dark:text-[#f6f6f8]">
    <div class="relative flex h-auto min-h-screen w-full flex-col font-display group/design-root overflow-x-hidden">
        <div class="layout-container flex h-full grow flex-col">
            <!-- Header -->
            <header
                class="sticky top-0 z-50 flex items-center justify-between whitespace-nowrap border-b border-solid border-b-primary/20 dark:border-b-primary/30 px-4 sm:px-10 lg:px-20 py-3 bg-background-light/80 dark:bg-background-dark/80 backdrop-blur-sm">
                <div class="flex items-center gap-4 text-celestial-blue dark:text-background-light">
                    <a href="index.html" class="flex items-center gap-4 hover:opacity-80 transition-opacity">
                        <div class="size-6 text-primary">
                            <span class="material-symbols-outlined !text-3xl">auto_stories</span>
                        </div>
                        <h2 class="text-xl font-bold leading-tight tracking-[-0.015em]">Gabriel the Brave</h2>
                    </a>
                </div>
                <div class="hidden md:flex flex-1 justify-end gap-8">
                    <div class="flex items-center gap-9">
                        <a class="text-celestial-blue dark:text-background-light text-sm font-medium leading-normal hover:text-primary dark:hover:text-primary"
                            href="index.html">Home</a>
                        <a class="text-celestial-blue dark:text-background-light text-sm font-medium leading-normal hover:text-primary dark:hover:text-primary"
                            href="news.html">Press</a>
                        <a class="text-celestial-blue dark:text-background-light text-sm font-medium leading-normal hover:text-primary dark:hover:text-primary"
                            href="activities.html">Activities</a>
                        <a class="text-celestial-blue dark:text-background-light text-sm font-medium leading-normal hover:text-primary dark:hover:text-primary"
                            href="about.html">About</a>
                    </div>
                    <a href="product.html"
                        class="flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-10 px-4 bg-primary text-white text-sm font-bold leading-normal tracking-[0.015em] hover:opacity-90">
                        <span class="truncate">Buy the Book</span>
                    </a>
                </div>
                <div class="md:hidden">
                    <button class="text-celestial-blue dark:text-background-light"
                        onclick="document.getElementById('mobile-menu').classList.toggle('hidden')">
                        <span class="material-symbols-outlined">menu</span>
                    </button>
                </div>
            </header>

            <!-- Mobile Menu -->
            <div id="mobile-menu"
                class="hidden md:hidden fixed inset-0 z-40 bg-background-light dark:bg-background-dark pt-20 px-4">
                <div class="flex flex-col gap-4">
                    <a class="text-xl font-medium" href="index.html">Home</a>
                    <a class="text-xl font-medium" href="news.html">Press</a>
                    <a class="text-xl font-medium" href="activities.html">Activities</a>
                    <a class="text-xl font-medium" href="about.html">About</a>
                    <a href="product.html" class="bg-primary text-white px-6 py-3 rounded-lg font-bold">Buy the Book</a>
                </div>
            </div>'''

# V4 Footer Template  
V4_FOOTER = '''<footer class="bg-celestial-blue dark:bg-gray-900 text-background-light mt-16">
                <div class="max-w-4xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
                        <div class="col-span-2 md:col-span-1">
                            <div class="flex items-center gap-3">
                                <div class="size-6 text-primary">
                                    <span class="material-symbols-outlined !text-3xl">auto_stories</span>
                                </div>
                                <h2 class="text-xl font-bold leading-tight">Gabriel the Brave</h2>
                            </div>
                            <div class="mt-4">
                                <img src="assets/images/logo_tymbr_wht.png" alt="Tymbr Books"
                                    style="height: 30px; opacity: 0.8;">
                            </div>
                        </div>
                        <div>
                            <h3 class="text-sm font-semibold tracking-wider uppercase text-gray-300">Navigation</h3>
                            <ul class="mt-4 space-y-2">
                                <li><a class="text-base text-gray-400 hover:text-white" href="index.html">Home</a></li>
                                <li><a class="text-base text-gray-400 hover:text-white" href="about.html">About</a></li>
                                <li><a class="text-base text-gray-400 hover:text-white"
                                        href="resources.html">Resources</a></li>
                            </ul>
                        </div>
                        <div>
                            <h3 class="text-sm font-semibold tracking-wider uppercase text-gray-300">Connect</h3>
                            <ul class="mt-4 space-y-2">
                                <li><a class="text-base text-gray-400 hover:text-white" href="product.html">Buy the
                                        Book</a></li>
                                <li><a class="text-base text-gray-400 hover:text-white" href="contact.html">Contact
                                        Us</a></li>
                                <li><a class="text-base text-gray-400 hover:text-white"
                                        href="mailto:Carteramon@gabrielthebrave.com">Carteramon@gabrielthebrave.com</a>
                                </li>
                                <li><span class="text-base text-gray-400">(817) 876-9627</span></li>
                                <li><span class="text-base text-gray-400">Dallas-Fort Worth, TX</span></li>
                            </ul>
                        </div>
                        <div>
                            <h3 class="text-sm font-semibold tracking-wider uppercase text-gray-300">Follow Us</h3>
                            <p class="mt-4 text-sm text-gray-400">Coming Soon</p>
                        </div>
                    </div>
                    <div class="mt-12 border-t border-gray-700 pt-8 text-center text-sm text-gray-400">
                        <p>&copy; <span id="year">2025</span> Gabriel the Brave. All rights reserved.</p>
                    </div>
                </div>
            </footer>
            <script>
                document.getElementById('year').textContent = new Date().getFullYear();
            </script>
        </div>
    </div>
</body>

</html>'''

def update_primary_color(content):
    """Update primary color from gold (#D4AF37) to blue (#2b6cee)"""
    return content.replace('"primary": "#D4AF37"', '"primary": "#2b6cee"')

def update_contact_info(content):
    """Update contact information to Carter's details"""
    # Replace fake address
    content = re.sub(r'123 Courage Ave.*?Faithville, Hope 45678', 'Dallas-Fort Worth, TX', content, flags=re.DOTALL)
    # Replace email
    content = content.replace('connect@gabrielthebrave.com', 'Carteramon@gabrielthebrave.com')
    return content

def main():
    print("Gabriel Website V4 Update Script - Version 1120v2")
    print("=" * 60)
    
    pages_to_update = [
        'product.html',
        'news.html',
        'activities.html',
        'resources.html',
        'curriculum_builder.html',
        'contact.html'
    ]
    
    for page in pages_to_update:
        file_path = V4_DIR / page
        if not file_path.exists():
            print(f"⚠️  {page} not found, skipping...")
            continue
            
        print(f"\nProcessing {page}...")
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Update primary color
            content = update_primary_color(content)
            
            # Update contact info
            content = update_contact_info(content)
            
            # TODO: Replace header/footer sections
            # This would require more sophisticated parsing to find the exact sections
            
            # Write back
            file_path.write_text(content, encoding='utf-8')
            print(f"✅ Updated {page}")
            
        except Exception as e:
            print(f"❌ Error updating {page}: {e}")
    
    print("\n" + "=" * 60)
    print("Update complete!")
    print("\nNOTE: Headers and footers need manual replacement.")
    print("Please copy from index.html lines 47-98 (header) and 269-324 (footer)")

if __name__ == "__main__":
    main()
