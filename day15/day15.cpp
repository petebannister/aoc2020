#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>

template <typename T>
void output(T v) {
	std::cout << v << std::endl;
}


uint32_t get_up_to(std::initializer_list<uint32_t> const& numbers, uint64_t lim)
{
	std::unordered_map<uint32_t, uint64_t> times(lim/16);
	uint64_t time = 0;
	uint32_t n;
	for (; time < numbers.size(); ++time) {
		n = numbers.begin()[time];
		times[n] = time;
	}
	--time;
	for (; time < (lim-1); ++time) { // lim -1?	
		if (0 == (time & 0x0FFFFF)) {
			output(time);
		}
		auto const last = n;
		auto found = times.find(n);
		if (found == times.end()) {
			n = 0;
		}
		else {
			n = static_cast<uint32_t>(time - found->second);
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
