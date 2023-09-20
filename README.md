# Assemble: Your Random Participant Pairing Script

This Python script is designed to read a CSV file containing participant information, shuffle the names randomly, and pair them up for an event. It's useful for creating random pairs of participants for activities or events.

## Prerequisites

- Python: You should have Python installed on your computer. If not, you can download it from [Python's official website](https://www.python.org/downloads/).

## Usage

1. **Data Collection**: Collect participant information using a Google Form and export the responses to a CSV file.

2. **Configure the Script**:
   - Open the script file (e.g., `pair_participants.py`) in a text editor.
   - Replace `'participants_responses.csv'` with the actual path to your CSV file containing participant data.
   - Modify `'Full Name'` to match the column name where participant names are stored in your CSV file, if different.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using the following command:
     ```
     python pair_participants.py
     ```

4. **View Pairs**: The script will print out pairs of participants, randomly paired from the CSV data. If there is an odd number of participants, one participant will be paired with "No partner available."

## Example Output

```
Pair: Alice Johnson and Bob Smith
Pair: Carol Davis and Dave Wilson
Pair: Eve Brown and Frank Lee
Pair: Grace White and Harry Adams
Pair: No partner available
```

## Customization

- If you have additional fields in your CSV data (e.g., email addresses, phone numbers), you can modify the script to include them in the pairs or adapt it to your specific needs.
- Feel free to customize the CSV file path and column name to match your data format.

## License

This script is provided under the [MIT License](LICENSE). You are free to use, modify, and distribute it as needed. 

## Acknowledgments

This script was created for the purpose of random participant pairing and can be a helpful tool for event organizers and educators.

