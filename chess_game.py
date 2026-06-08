import sys

# Initialize the chess board with standard piece setup
# Uppercase = White, Lowercase = Black
def create_board():
    return [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]

def print_board(board):
    print("\n   a  b  c  d  e  f  g  h")
    print("  +-----------------------+")
    for i, row in enumerate(board):
        # 8 minus index gives the correct chess rank number
        print(f"{8 - i} | " + "  ".join(row) + f" | {8 - i}")
    print("  +-----------------------+")
    print("   a  b  c  d  e  f  g  h\n")

def parse_notation(move_str):
    """Converts chess notation (like e2 e4) to board coordinates (row, col)"""
    try:
        start_str, end_str = move_str.split()
        
        start_col = ord(start_str[0]) - ord('a')
        start_row = 8 - int(start_str[1])
        
        end_col = ord(end_str[0]) - ord('a')
        end_row = 8 - int(end_str[1])
        
        return (start_row, start_col), (end_row, end_col)
    except (ValueError, IndexError):
        return None, None

def is_valid_basic_move(board, start, end, turn):
    sr, sc = start
    er, ec = end
    
    # Check boundaries
    if not (0 <= sr < 8 and 0 <= sc < 8 and 0 <= er < 8 and 0 <= ec < 8):
        return False
        
    piece = board[sr][sc]
    target = board[er][ec]
    
    # Check if moving an empty space
    if piece == ".":
        return False
        
    # Check turn (White = uppercase, Black = lowercase)
    if turn == "White" and not piece.isupper():
        return False
    if turn == "Black" and not piece.islower():
        return False
        
    # Can't capture your own piece
    if target != ".":
        if turn == "White" and target.isupper():
            return False
        if turn == "Black" and target.islower():
            return False
            
    return True

def main():
    board = create_board()
    turn = "White"
    
    print("Welcome to Terminal Chess!")
    print("Enter moves using standard coordinates separated by a space (e.g., 'e2 e4').")
    print("Type 'quit' to exit the game.")
    
    while True:
        print_board(board)
        print(f"{turn}'s turn.")
        move_input = input("Enter move: ").strip().lower()
        
        if move_input == 'quit':
            print("Thanks for playing!")
            sys.exit()
            
        start, end = parse_notation(move_input)
        
        if start is None or end is None:
            print("❌ Invalid input format! Use 'e2 e4'.")
            continue
            
        if is_valid_basic_move(board, start, end, turn):
            sr, sc = start
            er, ec = end
            
            # Execute the move
            board[er][ec] = board[sr][sc]
            board[sr][sc] = "."
            
            # Switch turns
            turn = "Black" if turn == "White" else "White"
        else:
            print("❌ Invalid move! Try again.")

if __name__ == "__main__":
    main()
