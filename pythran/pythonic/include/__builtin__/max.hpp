#ifndef PYTHONIC_INCLUDE_BUILTIN_MAX_HPP
#define PYTHONIC_INCLUDE_BUILTIN_MAX_HPP

#include "pythonic/include/utils/functor.hpp"
#include "pythonic/include/operator_/gt.hpp"
#include "pythonic/include/__builtin__/minmax.hpp"

PYTHONIC_NS_BEGIN

namespace __builtin__
{

  template <class... Types>
  auto max(Types &&... values)
      -> decltype(details::minmax(operator_::functor::lt{},
                                  std::forward<Types>(values)...));

  DEFINE_FUNCTOR(pythonic::__builtin__, max);
}
PYTHONIC_NS_END

#endif
