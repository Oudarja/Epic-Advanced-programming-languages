int: N;
set of int: POINT = 1..N;
set of int: TIME = 0..N;
array[POINT, POINT] of int: dist;

array[TIME] of var POINT: route;

constraint route[0] = 1;
constraint route[N] = 1;
% constraint route[1] < route[N-1];

include "globals.mzn";
constraint alldifferent(i in 1..N)(route[i]);
% constraint forall(i, j in 1..N where i < j)(
%   route[i] != route[j]
% );


var int: obj = sum([dist[route[i], route[i + 1]] | i in 0..N-1]);

solve
%   ::int_search(route, input_order, indomain_min)
%   ::int_search(route, first_fail, indomain_random)
  minimize(obj);

output ["SUM IS: ", show(obj), "\n", show(route)];
