class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board,
                                     vector<int>& click) {
        int m = board.size(), n = board[0].size();
        int dx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
        int dy[8] = {-1, 0, 1, 1, 1, 0, -1, -1};
        queue<pair<int, int>> q;
        int x = click[0], y = click[1];
        if (board[x][y] == 'M') {
            board[x][y] = 'X';
            return board;
        }
        q.push({x, y});
        while (!q.empty()) {
            auto [i, j] = q.front();
            q.pop();

            if (board[i][j] != 'E')
                continue;

            int mines = 0;
            for (int d = 0; d < 8; d++) {
                int ni = i + dx[d], nj = j + dy[d];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                    if (board[ni][nj] == 'M')
                        mines++;
                }
            }
            if (mines > 0) {
                board[i][j] = '0' + mines;
            } else {
                board[i][j] = 'B';
                for (int d = 0; d < 8; d++) {
                    int ni = i + dx[d], nj = j + dy[d];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                        if (board[ni][nj] == 'E') {
                            q.push({ni, nj});
                        }
                    }
                }
            }
        }
        return board;
    }
};