func searchMatrix(matrix [][]int, target int) bool {
    // For every row, perform binary search
    for _, col := range matrix {
        left, right := 0, len(col)-1

        for left <= right {
            mid := left + (right-left) / 2
            if col[mid] == target {
                return true
            } else if col[mid] < target {
                left = mid+1
            } else if col[mid] > target {
                right = mid-1
            }
        }
    }
    return false
}

