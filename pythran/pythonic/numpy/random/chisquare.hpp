#ifndef PYTHONIC_NUMPY_RANDOM_CHISQUARE_HPP
#define PYTHONIC_NUMPY_RANDOM_CHISQUARE_HPP

#include "pythonic/include/numpy/random/generator.hpp"
#include "pythonic/include/numpy/random/chisquare.hpp"

#include "pythonic/types/NoneType.hpp"
#include "pythonic/types/ndarray.hpp"
#include "pythonic/types/tuple.hpp"
#include "pythonic/utils/functor.hpp"

#include <algorithm>
#include <random>

PYTHONIC_NS_BEGIN
namespace numpy
{
  namespace random
  {

    template <class pS>
    types::ndarray<double, pS> chisquare(float df, pS const &shape)
    {
      types::ndarray<double, pS> result{shape, types::none_type()};
      std::chi_squared_distribution<double> distribution{df};
      std::generate(result.fbegin(), result.fend(),
                    [&]() { return distribution(details::generator); });
      return result;
    }

    auto chisquare(float df, long size)
        -> decltype(chisquare(df, types::array<long, 1>{{size}}))
    {

      return chisquare(df, types::array<long, 1>{{size}});
    }

    double chisquare(float df, types::none_type d)
    {
      return std::chi_squared_distribution<double>{static_cast<float>(df)}(
          details::generator);
    }
  }
}
PYTHONIC_NS_END

#endif
