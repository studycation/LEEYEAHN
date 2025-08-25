from step_1_2 import draw_board, init_board

def find_zero(board: list[list[int]]) -> tuple[int, int]:
    for row in range(len(board)): #행 검색
        for col in range(len(board[row])): #열 검색 
            if board[row][col] == 0:
                return row, col #0을 찾으면 0의 위치를 반환 

def move_zero_to(board: list[list[int]], direction: str) -> bool:
    row, col = find_zero(board) #0의 위치 
    if direction == "up":
        new_row, new_col = row -1, col #0을 위로 이동 
    if direction == "down":
        new_row, new_col = row +1, col #0을 아래로 이동 
    if direction == "left":
        new_row, new_col = row, col -1 #0을 왼쪽으로 이동 
    if direction == "right":
        new_row, new_col = row, col +1 #0을 오른쪽으로 이동

    #0의 새로운 위치가 보드 범위 내에 있는 결루 0을 이동하고, True를 반환함. 
    if 0 <=new_row < len(board) and 0 <=new_col<len(board[0]):
        zero, not_zero = board[row][col], board[new_row][new_col]
        board[row][col], board[new_row][new_col] = not_zero, zero
        return True 
    return False # 보드 범위를 벗어난 경우, False를 반환 

if __name__=="__main__":
    n_rows = n_cols = 3 #3행 3열 보드 
    board = init_board(n_rows, n_cols) #보드 초기화 
    draw_board(board) #보드 출력 
    #0을 상하좌우로 이동 
    for direction in ["up", "right", "down", "left"]:
        result = move_zero_to(board, direction)
        print(f"{direction=}, {result=}")
        draw_board(board)