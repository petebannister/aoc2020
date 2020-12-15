#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <deque>
#include <ctime>

template <typename T>
void output(T v) {
	std::cout << v << std::endl;
}


uint32_t get_up_to(std::initializer_list<uint32_t> const& numbers, uint32_t lim)
{
	std::vector<uint32_t> times(lim);
	uint32_t* p = &times[0];
	uint32_t time = 0;
	uint32_t n;
	for (; time < numbers.size(); ++time) {
		n = numbers.begin()[time]; 
		p[n] = time + 1;
	}
	for (; time < (lim); ++time) {
		auto& found = p[n];
		auto f = found;
		if (f == 0) {
			n = 0;
		}
		else {
			n = static_cast<uint32_t>(time - f);
		}
		found = time;
		//times[last] = time;
	}
	return n;
}

void main() {
	auto t = get_up_to({0,3,6}, 2020);
	output(t);
	//assert(t == 436);
	auto p1 = get_up_to({0,14,6,20,1,4}, 2020);

	//assert(p1 == 257);
	output(p1);

	auto c1 = clock();
	auto p2 = get_up_to({0,14,6,20,1,4}, 30000000);
	auto c2 = clock();
	auto run_time_ms = (1000 * (c2 - c1)) / CLOCKS_PER_SEC;
	output(p2);
	std::cout << "run time [ms]: " << run_time_ms<< std::endl;
}
