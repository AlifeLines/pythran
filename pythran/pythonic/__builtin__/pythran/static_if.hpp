#ifndef PYTHONIC_BUILTIN_PYTHRAN_STATIC_IF_HPP
#define PYTHONIC_BUILTIN_PYTHRAN_STATIC_IF_HPP

#include "pythonic/include/__builtin__/pythran/static_if.hpp"
#include "pythonic/utils/functor.hpp"
#include "pythonic/__builtin__/pythran/is_none.hpp"

PYTHONIC_NS_BEGIN

namespace __builtin__
{

  namespace pythran
  {

    template <class T, class F0, class F1>
    auto static_if(T const &cond, F0 f0, F1 f1)
        -> decltype(details::static_if<T>{cond}(f0, f1))
    {
      return details::static_if<T>{cond}(f0, f1);
    }
  }
}
PYTHONIC_NS_END

#endif
