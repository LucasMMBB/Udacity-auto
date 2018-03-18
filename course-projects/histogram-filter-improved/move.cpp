#include "headers/move.h"
#include "headers/zeros.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector< vector <float> > move(int dy, int dx, 
	vector < vector <float> > &beliefs) 
{
	int height, width, i, j;
	height = beliefs.size();
	width = beliefs[0].size();

	vector < vector <float> > newGrid;
  
  	// OPTIMIZATION: Use improved zeros function
	newGrid = zeros(height, width);

        // OPTIMIZATION: Eliminate any variables that aren't needed
  	for (i=0; i<height; i++) {
		for (j=0; j<width; j++) {
			newGrid[(i + dy + height) % height][(j + dx + width) % width] = beliefs[i][j];
		}
	}
	return newGrid;
}
