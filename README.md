# Digital-Clock
A simple and elegant digital clock application built with Python and tkinter.

# Digital Clock

## Description
A simple and elegant digital clock application built with Python and tkinter. This application displays the current time and date in a clean, easy-to-read format with a modern dark theme interface.

## Features
- Real-time clock display (HH:MM:SS format)
- Current date display
- Dark mode interface
- Auto-updating every second
- Clean and minimalist design
- Resizable window

## Prerequisites
Before running this application, make sure you have:
- Python 3.x installed
- tkinter library (usually comes with Python installation)

## Installation

1. Clone the repository or download the files:
```bash
git clone https://github.com/yourusername/digital-clock.git
```

2. Navigate to the project directory:
```bash
cd digital-clock
```

3. No additional packages need to be installed as the project uses only standard Python libraries.

## Usage

1. Run the application using Python:
```bash
python digital_clock.py
```

2. The clock will automatically start and display the current time and date.

3. To close the application, simply click the window's close button (X).

## Customization

You can customize the clock by modifying these values in the code:

### Window Size
```python
self.window.geometry("400x200")  # Change dimensions (width x height)
```

### Colors
```python
self.window.configure(bg='black')  # Change background color
foreground='cyan'  # Change text color
```

### Font
```python
font=('Arial', 50, 'bold')  # Change font family, size, and style
```

## Project Structure
```
digital_clock/
│
├── digital_clock.py    # Main application file
└── README.md          # Documentation
```

## How It Works

The application consists of three main components:

1. **Window Setup**: Creates the main application window using tkinter
2. **Time Display**: Shows the current time in HH:MM:SS format
3. **Date Display**: Shows the current date in Month DD, YYYY format

The clock updates every second using tkinter's `after()` method, which schedules the update function to run every 1000 milliseconds (1 second).

## Common Issues and Solutions

1. **Window doesn't appear**
   - Make sure you have Python installed correctly
   - Verify tkinter is installed with your Python distribution

2. **Clock shows wrong time**
   - The clock uses your system time, ensure your system time is set correctly

## Contributing

Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature requests.

Suggested areas for contribution:
- Adding alarm functionality
- Implementing different time zones
- Adding themes/color schemes
- Creating a 12-hour time format option

## License
This project is released under the MIT License. Feel free to use it for personal or commercial projects.

## Author
Mahmoud Eltayeb



