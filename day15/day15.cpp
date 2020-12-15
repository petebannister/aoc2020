#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <deque>

template <typename T>
void output(T v) {
	std::cout << v << std::endl;
}


uint32_t get_up_to(std::initializer_list<uint32_t> const& numbers, uint64_t lim)
{
	std::deque<uint32_t> times(4096);
	//std::unordered_map<uint32_t, uint64_t> times(lim); // / 16);
	uint64_t time = 0;
	uint32_t n;
	for (; time < numbers.size(); ++time) {
		n = numbers.begin()[time];
		times[n] = time + 1;
	}
	for (; time < (lim); ++time) { // lim -1?	
		if (0 == (time & 0x0FFFFF)) {
			output(time);
		}
		auto const last = n;
		if (n > times.size()) {
			times.resize(n + 1);
		}
		auto found = times[n];
		if (found == 0) {
			n = 0;
		}
		else {
			n = static_cast<uint32_t>(time - found);
		}
		times[last] = time;
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

	auto p2 = get_up_to({0,14,6,20,1,4}, 30000000);
	output(p2);
}
