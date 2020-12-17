#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstring>
#include <ctime>
#include <iostream>
#include <unordered_set>
#include <deque>
#include <vector>

#include "utils.h"

template <typename T>
void print(T v) {
	std::cout << v << std::endl;
}


using i32 = int32_t;
struct vec3 {
	i32 x, y, z;
	bool operator==(vec3 const& r) const {
		return (x == r.x && y == r.y && z == r.z);
	}
	vec3 operator+(vec3 const& v) const {
		return { x + v.x, y + v.y, z + v.z };
	}
	size_t hash() const {
		size_t h = x;
		h = h << 8 | h >> 24;
		h ^= y;
		h = h << 8 | h >> 24;
		h ^= z;
		return h;
	}
};
template<>
struct std::hash<vec3> {
	size_t operator() (vec3 const& v) const {
		return v.hash();
	}
};
struct vec4 {
	i32 x, y, z, w;
	bool operator==(vec4 const& r) const {
		return (x == r.x && y == r.y && z == r.z && w == r.w);
	}
	vec4 operator+(vec4 const& v) const {
		return { x + v.x, y + v.y, z + v.z , w + v.w };
	}
	size_t hash() const {
		size_t h = x;
		h = h << 8 | h >> 24;
		h ^= y;
		h = h << 8 | h >> 24;
		h ^= z;
		h = h << 8 | h >> 24;
		h ^= w;
		return h;
	}
};
template<>
struct std::hash<vec4> {
	size_t operator() (vec4 const& v) const {
		return v.hash();
	}
};

template <typename V> using hashset = std::unordered_set<V>;

auto make_seq3() {
	std::vector<vec3> seq;
	for (auto z : integers(-1, 2)) {
		for (auto y : integers(-1, 2)) {
			for (auto x : integers(-1, 2)) {
				if (x || y || z) {
					seq.push_back(vec3{ x,y,z });
				}
			}
		}
	}
	return seq;
}
auto make_seq4() {
	std::vector<vec4> seq;
	for (auto w : integers(-1, 2)) {
		for (auto z : integers(-1, 2)) {
			for (auto y : integers(-1, 2)) {
				for (auto x : integers(-1, 2)) {
					if (x || y || z || w) {
						seq.push_back(vec4{ x,y,z,w });
					}
				}
			}
		}
	}
	return seq;
}


template <typename V> V make_vec(i32 x, i32 y);
template <> vec3 make_vec<vec3>(i32 x, i32 y) {
	return vec3{ x, y, 0 };
}
template <> vec4 make_vec<vec4>(i32 x, i32 y) {
	return vec4{ x, y, 0, 0 };
}

template <typename V>
auto make_grid(std::string const& input) {
	hashset<V> grid;
	grid.reserve(1000000);
	i32 y = 0;
	for (auto&& line : split(input, '\n')) {
		i32 x = 0;
		for (auto ch : line) {
			if (ch == '#') {
				grid.insert(make_vec<V>(x, y));
			}
			++x;
		}
		++y;
	}
	return grid;
}

auto grid3(std::string const& input) {
	return make_grid<vec3>(input);
}
auto grid4(std::string const& input) {
	return make_grid<vec4>(input);
}

template <typename V>
size_t solve(hashset<V> grid, i32 steps, std::vector<V> const& seq)
{
	hashset<V> additions;
	hashset<V> removals;
	hashset<V> inactive;

	for (auto i : integers(0, steps)) {
		std::cout << "step:" << i << std::endl;

		additions.clear();
		removals.clear();
		inactive.clear();

		for (auto&& coord : grid) {
			i32 n = 0;
			for (auto&& dc : seq) {
				auto c2 = coord + dc;
				if (contains(grid, c2)) {
					++n;
				}
				else {
					inactive.insert(c2);
				}
			}
			// active cell:
			// If a cube is active and exactly 2 or 3 
			// of its neighbors are also active, the cube
			// remains active. Otherwise, the cube becomes inactive.
			if ((n != 2) && (n != 3) ) {
				removals.insert(coord);
			}
		}
				
		for (auto&& coord : inactive) {
			i32 n = 0;
			for (auto&& dc : seq) {
				auto c2 = coord + dc;
				if (contains(grid, c2)) {
					++n;
				}
			}
			// If a cube is inactive but exactly 3 of 
			// its neighbors are active, the cube becomes 
			// active. Otherwise, the cube remains inactive.
			if (n == 3) {
				additions.insert(coord);
			}
		}

		// update grid
		grid.insert(additions.begin(), additions.end());
		for (auto&& c : removals) {
			grid.erase(c);
		}
	}
		
	return grid.size();
}

std::string const input = R"~(...#...#
..##.#.#
###..#..
........
...##.#.
.#.####.
...####.
..##...#)~";

std::string const test = R"~(.#.
..#
###)~";

void main() {
	auto const seq3 = make_seq3();
	auto const seq4 = make_seq4();

	auto t1 = solve(grid3(test), 6, seq3);
	print(t1);
	assert(t1 == 112);

	auto t2 = solve(grid4(test), 6, seq4);
	print(t2);
	assert(t2 == 848);

	auto p1 = solve(grid3(input), 6, seq3);
	std::cout << "p1: " << p1 << std::endl;
	auto c1 = clock();
	auto p2 = solve(grid4(input), 6, seq4);
	auto c2 = clock();
	auto run_time_ms = (1000 * (c2 - c1)) / CLOCKS_PER_SEC;
	std::cout << "p2: " << p2 << std::endl;
	std::cout << "run time [ms]: " << run_time_ms << std::endl;
}
