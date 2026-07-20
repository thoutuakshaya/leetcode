class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

         rows = len(grid)
        cols = len(grid[0])
        total_elements = rows * cols
        
        # 2. Optimize k to prevent redundant full rotations
        k = k % total_elements
        if k == 0:
            return grid
            
        # 3. Create an empty result grid of the same size
        result = [[0] * cols for _ in range(rows)]
        
        # 4. Map each 2D element to its new 2D position via 1D math
        for r in range(rows):
            for c in range(cols):
                # Convert 2D index to a flattened 1D index
                current_1d_index = r * cols + c
                
                # Calculate the new 1D index after shifting k times
                new_1d_index = (current_1d_index + k) % total_elements
                
                # Convert the new 1D index back to 2D coordinates
                new_r = new_1d_index // cols
                new_c = new_1d_index % cols
                
                # Assign the value to the result grid
                result[new_r][new_c] = grid[r][c]
                
        return result