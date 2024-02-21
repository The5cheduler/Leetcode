class Solution {
    searchMatrix(matrix, target) {
        let row = matrix.length;
        let cols = matrix[0].length;

        let first = 0;
        let last = row - 1;

        while (first <= last) {
            row = Math.floor((first + last) / 2);

            if (target > matrix[row][cols - 1]) {
                first = row + 1;
            } else if (target < matrix[row][0]) {
                last = row - 1;
            } else {
                break;
            }
        }

        row = Math.floor((first + last) / 2);
        let left = 0;
        let right = cols - 1;

        while (left <= right) {
            let mid = Math.floor((left + right) / 2);

            if (target > matrix[row][mid]) {
                left = mid + 1;
            } else if (target < matrix[row][mid]) {
                right = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
