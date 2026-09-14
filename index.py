#!/usr/bin/env python3
"""
CRYPTIX SHADOW KERNEL HEX - Professional File Expansion Tool
Inspired by Zphisher, CamPhish, and PyPhisher
Author: Cryptix Security
Version: 1.0
"""

import os
import sys
import time
import math
import shutil
import argparse
from pathlib import Path

# Colors for terminal output (cross-platform)
class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    # Disable colors if not supported
    @staticmethod
    def disable():
        Colors.HEADER = Colors.BLUE = Colors.CYAN = Colors.GREEN = ''
        Colors.YELLOW = Colors.RED = Colors.MAGENTA = Colors.BOLD = ''
        Colors.UNDERLINE = Colors.END = ''

def check_color_support():
    """Check if terminal supports colors"""
    if os.name == 'nt':  # Windows
        if 'ANSICON' in os.environ:
            return True
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            return True
        except:
            Colors.disable()
            return False
    return True  # Unix-like systems support colors

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display CRYPTIX SHADOW KERNEL HEX banner"""
    banner = f"""
{Colors.RED}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║    {Colors.CYAN}██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗██╗  ██╗{Colors.RED}              ║
║    {Colors.CYAN}██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║╚██╗██╔╝{Colors.RED}              ║
║    {Colors.CYAN}██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║ ╚███╔╝ {Colors.RED}              ║
║    {Colors.CYAN}██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║ ██╔██╗ {Colors.RED}              ║
║    {Colors.CYAN}╚██████╗██║  ██║   ██║   ██║        ██║   ██║██╔╝ ██╗{Colors.RED}              ║
║    {Colors.CYAN} ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝╚═╝  ╚═╝{Colors.RED}              ║
║                                                                      ║
║    {Colors.GREEN}███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗{Colors.RED}              ║
║    {Colors.GREEN}██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║{Colors.RED}              ║
║    {Colors.GREEN}███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║{Colors.RED}              ║
║    {Colors.GREEN}╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║{Colors.RED}              ║
║    {Colors.GREEN}███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝{Colors.RED}              ║
║    {Colors.GREEN}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ {Colors.RED}              ║
║                                                                      ║
║    {Colors.YELLOW}██╗  ██╗███████╗██████╗ ███╗   ██╗███████╗██╗     {Colors.RED}              ║
║    {Colors.YELLOW}██║ ██╔╝██╔════╝██╔══██╗████╗  ██║██╔════╝██║     {Colors.RED}              ║
║    {Colors.YELLOW}█████╔╝ █████╗  ██████╔╝██╔██╗ ██║█████╗  ██║     {Colors.RED}              ║
║    {Colors.YELLOW}██╔═██╗ ██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝  ██║     {Colors.RED}              ║
║    {Colors.YELLOW}██║  ██╗███████╗██║  ██║██║ ╚████║███████╗███████╗{Colors.RED}              ║
║    {Colors.YELLOW}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝{Colors.RED}              ║
║                                                                      ║
║    {Colors.MAGENTA}██╗  ██╗███████╗██╗  ██╗{Colors.RED}                                        ║
║    {Colors.MAGENTA}██║  ██║██╔════╝╚██╗██╔╝{Colors.RED}                                        ║
║    {Colors.MAGENTA}███████║█████╗   ╚███╔╝ {Colors.RED}                                        ║
║    {Colors.MAGENTA}██╔══██║██╔══╝   ██╔██╗ {Colors.RED}                                        ║
║    {Colors.MAGENTA}██║  ██║███████╗██╔╝ ██╗{Colors.RED}                                        ║
║    {Colors.MAGENTA}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Colors.RED}                                        ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║{Colors.BLUE}                 CRYPTIX SHADOW KERNEL HEX v1.0{Colors.RED}                           ║
║{Colors.BLUE}              Professional File Expansion Tool{Colors.RED}                            ║
║{Colors.BLUE}                    Maximum Size: 4GB{Colors.RED}                                     ║
╚══════════════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.RED}{Colors.BOLD}⚠️  FOR EDUCATIONAL & SECURITY TESTING PURPOSES ONLY  ⚠️{Colors.END}
"""
    print(banner)

def fake_loading_animation(message, duration=2):
    """Display professional loading animation"""
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
                 "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", 
                 "[■■■■■■■■■■]"]
    
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{Colors.CYAN}{message} {animation[i % len(animation)]}{Colors.END}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print()

def parse_size_input(size_str):
    """
    Parse user input for file size
    Supports formats: 1, 1GB, 0.5GB, 2.5, etc.
    """
    try:
        # Remove whitespace and convert to uppercase
        size_str = size_str.strip().upper()
        
        # Remove 'GB' suffix if present
        if size_str.endswith('GB'):
            size_str = size_str[:-2]
        
        # Convert to float
        size_gb = float(size_str)
        
        # Validate range (0.1GB to 4GB)
        if size_gb < 0.1:
            print(f"{Colors.RED}[-] Error: Size must be at least 0.1GB{Colors.END}")
            return None
        elif size_gb > 4:
            print(f"{Colors.RED}[-] Error: Maximum size is 4GB{Colors.END}")
            return None
        
        return size_gb
    except ValueError:
        print(f"{Colors.RED}[-] Error: Invalid size format. Use numbers like 1, 0.5, 2GB{Colors.END}")
        return None

def get_file_size(file_path):
    """Get file size in human-readable format"""
    size_bytes = os.path.getsize(file_path)
    return size_bytes, format_size(size_bytes)

def format_size(size_bytes):
    """Convert bytes to human-readable format"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return f"{s} {size_names[i]}"

def create_progress_bar(progress, width=50):
    """Create a visual progress bar"""
    filled = int(width * progress // 100)
    bar = f"{Colors.GREEN}{'█' * filled}{Colors.YELLOW}{'▒' * (width - filled)}{Colors.END}"
    return f"[{bar}] {progress:.1f}%"

def expand_file(file_path, target_size_gb):
    """
    Expand file to target size with progress bar
    Maximum size: 4GB
    """
    try:
        # Get original file info
        orig_size_bytes, orig_size_hr = get_file_size(file_path)
        
        # Calculate target size in bytes
        target_size_bytes = int(target_size_gb * 1024 * 1024 * 1024)
        
        # Validate target size
        if target_size_bytes <= orig_size_bytes:
            print(f"{Colors.YELLOW}[!] Warning: Target size is smaller than or equal to original size{Colors.END}")
            print(f"{Colors.YELLOW}[!] No changes will be made{Colors.END}")
            return False
        
        if target_size_bytes > 4 * 1024 * 1024 * 1024:  # 4GB in bytes
            print(f"{Colors.RED}[-] Error: Maximum file size is 4GB{Colors.END}")
            return False
        
        # Create output filename
        file_path = Path(file_path)
        output_path = file_path.parent / f"{file_path.stem}_expanded{file_path.suffix}"
        
        print(f"\n{Colors.CYAN}[*] Target File: {file_path.name}{Colors.END}")
        print(f"{Colors.CYAN}[*] Original Size: {orig_size_hr}{Colors.END}")
        print(f"{Colors.CYAN}[*] Target Size: {target_size_gb} GB{Colors.END}")
        print(f"{Colors.CYAN}[*] Output File: {output_path.name}{Colors.END}\n")
        
        # Fake loading animation (pro-style)
        fake_loading_animation("[*] Initializing CRYPTIX SHADOW KERNEL HEX", 1.5)
        
        # Copy original file to new location
        print(f"{Colors.YELLOW}[*] Creating base file...{Colors.END}")
        shutil.copy2(file_path, output_path)
        
        # Calculate how many bytes to add
        bytes_to_add = target_size_bytes - orig_size_bytes
        
        # Open file in append binary mode
        with open(output_path, 'ab') as f:
            # Write in chunks with progress bar
            chunk_size = 1024 * 1024  # 1MB chunks
            chunks_written = 0
            total_chunks = math.ceil(bytes_to_add / chunk_size)
            
            print(f"{Colors.CYAN}[*] Expanding file...{Colors.END}\n")
            
            for i in range(total_chunks):
                # Calculate chunk size for last chunk
                current_chunk_size = min(chunk_size, bytes_to_add - (i * chunk_size))
                
                # Write null bytes
                f.write(b'\0' * current_chunk_size)
                chunks_written += 1
                
                # Update progress
                progress = (i + 1) / total_chunks * 100
                sys.stdout.write(f"\r{create_progress_bar(progress)}")
                sys.stdout.flush()
                
                # Small delay to show progress (removed for very large files)
                if total_chunks > 100:  # Only for files > 100MB
                    time.sleep(0.001)
            
            print(f"\n\n{Colors.GREEN}[✓] File expansion completed!{Colors.END}")
        
        # Get final file size
        final_size_bytes, final_size_hr = get_file_size(output_path)
        
        # Display results
        print(f"\n{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.GREEN}[✓] SUCCESS: File expanded successfully{Colors.END}")
        print(f"{Colors.CYAN}[*] Original size: {orig_size_hr}{Colors.END}")
        print(f"{Colors.CYAN}[*] New size: {final_size_hr}{Colors.END}")
        print(f"{Colors.CYAN}[*] Saved as: {output_path}{Colors.END}")
        print(f"{Colors.BOLD}{'='*60}{Colors.END}\n")
        
        return True
        
    except PermissionError:
        print(f"{Colors.RED}[-] Error: Permission denied. Cannot write to file.{Colors.END}")
        return False
    except Exception as e:
        print(f"{Colors.RED}[-] Error: {str(e)}{Colors.END}")
        return False

def main():
    """Main function"""
    # Check color support
    check_color_support()
    
    # Clear screen and show banner
    clear_screen()
    print_banner()
    
    print(f"{Colors.YELLOW}[*] Welcome to CRYPTIX SHADOW KERNEL HEX{Colors.END}")
    print(f"{Colors.YELLOW}[*] This tool expands files up to 4GB{Colors.END}\n")
    
    # Get file path from user
    while True:
        file_path = input(f"{Colors.BOLD}[?] Enter path to file: {Colors.END}").strip()
        
        if not file_path:
            print(f"{Colors.RED}[-] Error: File path cannot be empty{Colors.END}")
            continue
        
        if not os.path.exists(file_path):
            print(f"{Colors.RED}[-] Error: File does not exist{Colors.END}")
            continue
        
        if not os.path.isfile(file_path):
            print(f"{Colors.RED}[-] Error: Path is not a file{Colors.END}")
            continue
        
        break
    
    # Get target size
    while True:
        size_input = input(f"{Colors.BOLD}[?] Enter target size (GB, max 4GB): {Colors.END}").strip()
        target_size = parse_size_input(size_input)
        
        if target_size is not None:
            break
    
    # Confirm operation
    print(f"\n{Colors.YELLOW}[!] You are about to expand: {os.path.basename(file_path)}{Colors.END}")
    print(f"{Colors.YELLOW}[!] Target size: {target_size} GB{Colors.END}")
    
    confirm = input(f"{Colors.BOLD}[?] Proceed? (yes/no): {Colors.END}").strip().lower()
    
    if confirm in ['yes', 'y']:
        # Perform file expansion
        expand_file(file_path, target_size)
    else:
        print(f"{Colors.YELLOW}[!] Operation cancelled{Colors.END}")
    
    # Exit with pro-style message
    print(f"\n{Colors.MAGENTA}[*] Thank you for using CRYPTIX SHADOW KERNEL HEX{Colors.END}")
    print(f"{Colors.MAGENTA}[*] Stay secure, stay anonymous{Colors.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}[!] Operation interrupted by user{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[-] Unexpected error: {str(e)}{Colors.END}")
        sys.exit(1)
