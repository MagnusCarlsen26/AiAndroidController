from utils.updateConfig import updateConfig

def setScreenResolution():
    print("\nCommon resolutions:")
    print("1. 1920x1080 (Full HD)")
    print("2. 2560x1440 (QHD)")
    print("3. 3840x2160 (4K)")
    print("4. Custom (enter manually)")
    
    resolutionChoice = int(input("\nEnter your choice: "))

    if resolutionChoice == 1: resolution = "1920x1080"
    elif resolutionChoice == 2: resolution = "2560x1440"
    elif resolutionChoice == 3: resolution = "3840x2160"
    elif resolutionChoice == 4: resolution = input("Enter custom resolution (e.g., 1920x1080): ")
    else:
        print("Invalid choice. Please try again.")
        return
    
    try:
        width, height = map(int, resolution.split('x'))
        updateConfig({"resolution": {"width": width, "height": height}})
        print(f"Screen resolution set to: {width}x{height}")
    except ValueError:
        print("Invalid resolution format. Please use 'WIDTHxHEIGHT' (e.g., 1920x1080).")
