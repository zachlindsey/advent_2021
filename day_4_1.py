
input_file = "day_4_input.txt"

with open(input_file) as f:
	lines = f.readlines()

	numbers = list(map(int, lines[0].strip().split(',')))

	boards = [lines[i:i+5] for i in range(2,len(lines),6)]

	def clean_board(board_strings):
		result = []
		for line in board_strings:
			line = line.strip().split(' ')
			line = filter(lambda x: x != '', line)
			line = list(map(int, line))
			result.append(line)
		return result

	boards = list(map(clean_board, boards))

BOARD_SIZE = len(boards[0][0])
cur_boards = set(range(len(boards)))
board_trackers = []
for _ in range(len(boards)):
	board_trackers.append([0 for _ in range(2*BOARD_SIZE)])
	# first N numbers count rows
	# next N numbers count cols
	

def update_board(board, board_index, num):
	for i, row in enumerate(board):
		for j, val in enumerate(row):
			if val == num:
				board_trackers[board_index][i] += 1
				board_trackers[board_index][BOARD_SIZE+j] += 1
				
def is_winner(board_index):
	return max(board_trackers[board_index]) == BOARD_SIZE
	
def get_board_score(board, already_called):
	board_score = 0

	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			if board[i][j] not in already_called:
				board_score += board[i][j]
	return board_score


already_called = set()
first_winners = set()
last_num = None

for num in numbers:
	if num in already_called:
		continue


	if len(cur_boards) == 0:
		max_score = 0
		# grab the winners from the last round
		for winner in winners:
			board = boards[winner]
			board_score = get_board_score(board, already_called)
			max_score = max(max_score, board_score)

		print('last winner:')
		print('num', last_num)
		print('board score:', board_score)
		print('product', last_num*board_score)
		break


	winners = set()
	already_called.add(num)
	for i in cur_boards:
		board = boards[i]
		update_board(board, i, num)
		if is_winner(i):
			winners.add(i)

	for i in winners:
		cur_boards.remove(i)


	if len(winners) > 0 and len(first_winners) == 0:

		first_winners = winners.copy()

		max_score = 0
		for winner in first_winners:
			board = boards[winner]
			board_score = get_board_score(board, already_called)
			max_score = max(max_score, board_score)

		print('First winner:')
		print('num', num)
		print('board score:', board_score)
		print('product', num*board_score)

	last_num = num


