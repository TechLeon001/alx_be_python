from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    """Calculate and return a future date by adding days to the current date"""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    return formatted_future

def main():
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days = int(input("\nEnter the number of days to add to the current date: "))
        future_date = calculate_future_date(days)
        print(f"Future date: {future_date}")
    except ValueError:
        print("Error: Please enter a valid integer for number of days.")

if __name__ == "__main__":
    main()
