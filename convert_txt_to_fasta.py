def convert_to_fasta(input_file, output_file):
    """
    Convert a file with one sequence per line into a FASTA format file.

    :param input_file: Path to the input file containing sequences (one per line).
    :param output_file: Path to the output FASTA file.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            sequence_number = 1
            for line in infile:
                sequence = line.strip()  # Remove leading/trailing whitespace
                if sequence:  # Skip empty lines
                    # Write the FASTA header
                    outfile.write(f">seq_{sequence_number}\n")
                    # Write the sequence
                    outfile.write(f"{sequence}\n")
                    sequence_number += 1
        print(f"FASTA file has been created and saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Input file containing sequences (one per line)
    input_file = input("Enter the path to the input file: ")

    # Output FASTA file
    output_file = input("Enter the path to save the FASTA file: ")

    # Convert to FASTA format
    convert_to_fasta(input_file, output_file)
