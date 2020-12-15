#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <cstring>
#include <ctime>

template <typename T>
void output(T v) {
	std::cout << v << std::endl;
}


uint32_t get_up_to(std::initializer_list<uint32_t> const& numbers, uint32_t lim)
{
	std::unique_ptr<uint32_t[]> times_data(new uint32_t[lim]);
	uint32_t* times = times_data.get();
	memset(&times[0], 0, lim * sizeof(times[0]));

	uint32_t time = 0;
	uint32_t n;
	for (; time < numbers.size(); ++time) {
		n = numbers.begin()[time]; 
		times[n] = time + 1;
	}
	for (; time < lim; ++time) {
		auto* p_last = &times[n];
		auto last = *p_last;
		if (last == 0) {
			n = 0;
		}
		else {
			n = static_cast<uint32_t>(time - last);
		}
		*p_last = time;
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
