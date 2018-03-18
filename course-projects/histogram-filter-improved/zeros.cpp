#include "headers/zeros.h"

using namespace std;

vector < vector <float> > zeros(int height, int width) {
	int row, col;
  
	// OPTIMIZATION: Reserve space in memory for vectors
	vector < vector <float> > newGrid;
	vector <float> newRow;

	newGrid.reserve(height);
	newRow.reserve(width);

  	// OPTIMIZATION: nested for loop not needed
    // because every row in the matrix is exactly the same
	for (col = 0; col < width; col++) {
		newRow.push_back(0.0);
	}
	for (row = 0; row < height; row++) {
		newGrid.push_back(newRow);
	}
	return newGrid;

	// Optimized time: from O(m*n) to O(m+n)
}