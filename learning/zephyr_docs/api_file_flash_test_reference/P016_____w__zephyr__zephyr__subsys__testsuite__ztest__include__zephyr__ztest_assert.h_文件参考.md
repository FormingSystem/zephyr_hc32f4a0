---
id: learning.zephyr-docs.api-file-flash-test-reference.page-16
title: ____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest_assert.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_ztest\_\_include\_\_zephyr\_\_ztest\_assert.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr测试框架（Testing Framework）的断言宏。

<a id="details"></a>

```c
#include <stdarg.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <zephyr/sys/util.h>
#include <zephyr/tc_util.h>
#include <zephyr/ztest.h>
```

查看此文件的源码。

Zephyr测试框架（Testing Framework）的断言宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.1\_宏定义（Macros）

<a id="r_ga0911ad9e94cdf1fe011d21316683ee7f"></a>

```c
#define zassert(cond, default_msg, ...)
```

相关声明：[zassert](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga0911ad9e94cdf1fe011d21316683ee7f)。

<a id="r_ga5a4319eec770be532f34acb86e022c48"></a>

```c
#define zassume(cond, default_msg, ...)
```

相关声明：[zassume](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga5a4319eec770be532f34acb86e022c48)。

<a id="r_ga7bd837a8164123e3a06795b9f87a308d"></a>

```c
#define zexpect(cond, default_msg, ...)
```

相关声明：[zexpect](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga7bd837a8164123e3a06795b9f87a308d)。

<a id="r_ga300684a6b56e73e2cad6fd7458541129"></a>

```c
#define zassert_unreachable(...)
```

相关声明：[zassert_unreachable](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga300684a6b56e73e2cad6fd7458541129)。

断言（Assert）执行不会到达此次函数调用。

<a id="r_gaeebddde19012223e3d5e853a1dac3ac5"></a>

```c
#define zassert_true(cond, ...)
```

相关声明：[zassert_true](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gaeebddde19012223e3d5e853a1dac3ac5)。

断言（Assert）cond 为真（True）。

<a id="r_ga7330d1794fb961e07ee40294019dead0"></a>

```c
#define zassert_false(cond, ...)
```

相关声明：[zassert_false](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga7330d1794fb961e07ee40294019dead0)。

断言（Assert）cond 为假（False）。

<a id="r_gade40e2ec78ec813739e7725524fae7f0"></a>

```c
#define zassert_ok(cond, ...)
```

相关声明：[zassert_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gade40e2ec78ec813739e7725524fae7f0)。

断言（Assert）cond 为 0（成功，Success）。

<a id="r_gafe0e2609f77906ab0caddc31448a4fc8"></a>

```c
#define zassert_not_ok(cond, ...)
```

相关声明：[zassert_not_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gafe0e2609f77906ab0caddc31448a4fc8)。

断言（Assert）cond 不为 0（失败，Failure）。

<a id="r_gac0839891fd8bb7313b98551465e04c19"></a>

```c
#define zassert_is_null(ptr, ...)
```

相关声明：[zassert_is_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gac0839891fd8bb7313b98551465e04c19)。

断言（Assert）ptr 为 NULL。

<a id="r_ga849adad4afe893a7ae3dc2fbe750dc00"></a>

```c
#define zassert_not_null(ptr, ...)
```

相关声明：[zassert_not_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga849adad4afe893a7ae3dc2fbe750dc00)。

断言（Assert）ptr 不为 NULL。

<a id="r_gacd075c7ee4dc2d64701bd3098a31b673"></a>

```c
#define zassert_equal(a, b, ...)
```

相关声明：[zassert_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gacd075c7ee4dc2d64701bd3098a31b673)。

断言（Assert）a 等于 b。

<a id="r_ga43f306bf33d5e837b8927df16b82a363"></a>

```c
#define zassert_not_equal(a, b, ...)
```

相关声明：[zassert_not_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga43f306bf33d5e837b8927df16b82a363)。

断言（Assert）a 不等于 b。

<a id="r_gabf20273fcba9cc45939a9f7db77f0bfc"></a>

```c
#define zassert_equal_ptr(a, b, ...)
```

相关声明：[zassert_equal_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gabf20273fcba9cc45939a9f7db77f0bfc)。

断言（Assert）a 等于 b。

<a id="r_gacc930af1a66e8533c5eca9526e198b4b"></a>

```c
#define zassert_within(a, b, d, ...)
```

相关声明：[zassert_within](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gacc930af1a66e8533c5eca9526e198b4b)。

断言（Assert）a 与 b 的差值在容差（Delta）d 以内。

<a id="r_ga2b6b41de3e4856b21458febab3261b91"></a>

```c
#define zassert_between_inclusive(a, l, u, ...)
```

相关声明：[zassert_between_inclusive](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga2b6b41de3e4856b21458febab3261b91)。

断言（Assert）a 大于或等于 l 且小于或等于 u。

<a id="r_gabbfcf6345172387326d35b5d0e2bb051"></a>

```c
#define zassert_mem_equal(...)
```

相关声明：[zassert_mem_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gabbfcf6345172387326d35b5d0e2bb051)。

断言（Assert）两个内存缓冲区（Memory Buffers）的内容相同。

<a id="r_ga30e5fefa185944d3e949d4023c2eea27"></a>

```c
#define zassert_mem_equal__(buf, exp, size, ...)
```

相关声明：[zassert_mem_equal__](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga30e5fefa185944d3e949d4023c2eea27)。

内部断言（Assert）两个内存缓冲区（Memory Buffers）的内容相同。

<a id="r_ga382017945a8c409e885cad8d0909b197"></a>

```c
#define zassert_str_equal(s1, s2, ...)
```

相关声明：[zassert_str_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga382017945a8c409e885cad8d0909b197)。

断言（Assert）两个字符串（Strings）的内容相同。

<a id="r_ga6f5778ed8c1205126f7dcafb6eb26905"></a>

```c
#define zassume_true(cond, ...)
```

相关声明：[zassume_true](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga6f5778ed8c1205126f7dcafb6eb26905)。

假定（Assume）cond 为真（True）。

<a id="r_ga5acf4256e5af3afaed06da7400dc3ad5"></a>

```c
#define zassume_false(cond, ...)
```

相关声明：[zassume_false](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga5acf4256e5af3afaed06da7400dc3ad5)。

假定（Assume）cond 为假（False）。

<a id="r_ga9c6d1c701dd2d50027bf5e24b7567ae4"></a>

```c
#define zassume_ok(cond, ...)
```

相关声明：[zassume_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga9c6d1c701dd2d50027bf5e24b7567ae4)。

假定（Assume）cond 为 0（成功，Success）。

<a id="r_ga539831d2f42cc991a8295b388ec12846"></a>

```c
#define zassume_not_ok(cond, ...)
```

相关声明：[zassume_not_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga539831d2f42cc991a8295b388ec12846)。

假定（Assume）cond 不为 0（失败，Failure）。

<a id="r_ga3c5b1814deb5974e8ba0af961b516fa0"></a>

```c
#define zassume_is_null(ptr, ...)
```

相关声明：[zassume_is_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga3c5b1814deb5974e8ba0af961b516fa0)。

假定（Assume）ptr 为 NULL。

<a id="r_ga24f4144edf5cef493c88872c7d56900e"></a>

```c
#define zassume_not_null(ptr, ...)
```

相关声明：[zassume_not_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga24f4144edf5cef493c88872c7d56900e)。

假定（Assume）ptr 不为 NULL。

<a id="r_ga88c2a3153568a6f621b88dd6ceeb48d6"></a>

```c
#define zassume_equal(a, b, ...)
```

相关声明：[zassume_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga88c2a3153568a6f621b88dd6ceeb48d6)。

假定（Assume）a 等于 b。

<a id="r_ga0d90bb874c3135ffee870a4b61607853"></a>

```c
#define zassume_not_equal(a, b, ...)
```

相关声明：[zassume_not_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga0d90bb874c3135ffee870a4b61607853)。

假定（Assume）a 不等于 b。

<a id="r_ga78d6fbbf5eb13b32a5164053811b6cca"></a>

```c
#define zassume_equal_ptr(a, b, ...)
```

相关声明：[zassume_equal_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga78d6fbbf5eb13b32a5164053811b6cca)。

假定（Assume）a 等于 b。

<a id="r_gad808c91e07e6c27b2e28ec7e04e03854"></a>

```c
#define zassume_within(a, b, d, ...)
```

相关声明：[zassume_within](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gad808c91e07e6c27b2e28ec7e04e03854)。

假定（Assume）a 与 b 的差值在容差（Delta）d 以内。

<a id="r_gacff02eeba8dd334b3727dbe2036617e3"></a>

```c
#define zassume_between_inclusive(a, l, u, ...)
```

相关声明：[zassume_between_inclusive](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gacff02eeba8dd334b3727dbe2036617e3)。

假定（Assume）a 大于或等于 l 且小于或等于 u。

<a id="r_ga62be45256399530167745e71226e4a37"></a>

```c
#define zassume_mem_equal(...)
```

相关声明：[zassume_mem_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga62be45256399530167745e71226e4a37)。

假定（Assume）两个内存缓冲区（Memory Buffers）的内容相同。

<a id="r_gaaed6045f194ead4ffe1dd72a6fa5175d"></a>

```c
#define zassume_mem_equal__(buf, exp, size, ...)
```

相关声明：[zassume_mem_equal__](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gaaed6045f194ead4ffe1dd72a6fa5175d)。

内部假定（Assume）两个内存缓冲区（Memory Buffers）的内容相同。

<a id="r_ga33a9cd37d321f1a421a1328e67b04788"></a>

```c
#define zassume_str_equal(s1, s2, ...)
```

相关声明：[zassume_str_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga33a9cd37d321f1a421a1328e67b04788)。

假定（Assume）两个字符串（Strings）的内容相同。

<a id="r_gaef66b2764b6086dfbe8cbc933a8cfdc3"></a>

```c
#define zexpect_true(cond, ...)
```

相关声明：[zexpect_true](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaef66b2764b6086dfbe8cbc933a8cfdc3)。

预期（Expect）cond 为真（True）；否则将测试标记为失败，但继续执行测试。

<a id="r_ga619bd320e39799414383a228dc2d8299"></a>

```c
#define zexpect_false(cond, ...)
```

相关声明：[zexpect_false](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga619bd320e39799414383a228dc2d8299)。

预期（Expect）cond 为假（False）；否则将测试标记为失败，但继续执行测试。

<a id="r_gaab325ee22058252c6a1c3243f3226657"></a>

```c
#define zexpect_ok(cond, ...)
```

相关声明：[zexpect_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaab325ee22058252c6a1c3243f3226657)。

预期（Expect）cond 为 0（成功，Success）；否则将测试标记为失败，但继续执行测试。

<a id="r_gabde5406775f05d5fcd135eb926969004"></a>

```c
#define zexpect_not_ok(cond, ...)
```

相关声明：[zexpect_not_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gabde5406775f05d5fcd135eb926969004)。

预期（Expect）cond 不为 0（失败，Failure）；否则将测试标记为失败，但继续执行测试。

<a id="r_ga10b2c904f1c68b816eae2ad53e2b9f90"></a>

```c
#define zexpect_is_null(ptr, ...)
```

相关声明：[zexpect_is_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga10b2c904f1c68b816eae2ad53e2b9f90)。

预期（Expect）ptr 为 NULL；否则将测试标记为失败，但继续执行测试。

<a id="r_gaa51053fe2a07c6417db7952d7a594798"></a>

```c
#define zexpect_not_null(ptr, ...)
```

相关声明：[zexpect_not_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaa51053fe2a07c6417db7952d7a594798)。

预期（Expect）ptr 不为 NULL；否则将测试标记为失败，但继续执行测试。

<a id="r_ga5ba65dbf95c204ed60694c5757db247f"></a>

```c
#define zexpect_equal(a, b, ...)
```

相关声明：[zexpect_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga5ba65dbf95c204ed60694c5757db247f)。

预期（Expect）a 等于 b；否则将测试标记为失败，但继续执行测试。

<a id="r_ga31d83ab89828a03aebe0d0dc003f5232"></a>

```c
#define zexpect_not_equal(a, b, ...)
```

相关声明：[zexpect_not_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga31d83ab89828a03aebe0d0dc003f5232)。

预期（Expect）a 不等于 b；否则将测试标记为失败，但继续执行测试。

<a id="r_gabf791d13c5781fc2215289d6dd925b3e"></a>

```c
#define zexpect_equal_ptr(a, b, ...)
```

相关声明：[zexpect_equal_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gabf791d13c5781fc2215289d6dd925b3e)。

预期（Expect）a 等于 b；否则将测试标记为失败，但继续执行测试。

<a id="r_ga907afb07269bbc444a3d8ffee46839b5"></a>

```c
#define zexpect_within(a, b, delta, ...)
```

相关声明：[zexpect_within](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga907afb07269bbc444a3d8ffee46839b5)。

预期（Expect）a 与 b 的差值在容差（Delta）d 以内；否则将测试标记为失败，但继续执行测试。

<a id="r_gac37ebea6a9c71e3666a4911ceea5c913"></a>

```c
#define zexpect_between_inclusive(a, lower, upper, ...)
```

相关声明：[zexpect_between_inclusive](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gac37ebea6a9c71e3666a4911ceea5c913)。

预期（Expect）a 大于或等于 l 且小于或等于 u；否则将测试标记为失败，但继续执行测试。

<a id="r_gaee52264e5f92a606a2a85f5fbb0a85fb"></a>

```c
#define zexpect_mem_equal(buf, exp, size, ...)
```

相关声明：[zexpect_mem_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaee52264e5f92a606a2a85f5fbb0a85fb)。

预期（Expect）两个内存缓冲区（Memory Buffers）的内容相同；否则将测试标记为失败，但继续执行测试。

<a id="r_gacd5ef284610ca2027fc2e892243dfd38"></a>

```c
#define zexpect_str_equal(s1, s2, ...)
```

相关声明：[zexpect_str_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gacd5ef284610ca2027fc2e892243dfd38)。

预期（Expect）两个字符串（Strings）的内容相同；否则将测试标记为失败，但继续执行测试。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.2\_函数（Functions）

<a id="r_a06a081e3d716be7e024973cbf305c14b"></a>

```c
const char * ztest_relative_filename (const char *file)
```

相关声明：[ztest_relative_filename](#a06a081e3d716be7e024973cbf305c14b)。

<a id="r_acd6eb423f54dce8544f7c3b1618c0374"></a>

```c
void ztest_test_fail (void)
```

相关声明：[ztest_test_fail](#acd6eb423f54dce8544f7c3b1618c0374)。

<a id="r_ada3b1fcfa71db1bf7787c03ff45256d5"></a>

```c
void ztest_test_skip (void)
```

相关声明：[ztest_test_skip](#ada3b1fcfa71db1bf7787c03ff45256d5)。

<a id="r_a5c6bb493c88f7426a827889526dc0772"></a>

```c
void ztest_test_expect_fail (void)
```

相关声明：[ztest_test_expect_fail](#a5c6bb493c88f7426a827889526dc0772)。

<a id="r_a17537c79021fbc12e56b72ccec4b99c5"></a>

```c
void ztest_skip_failed_assumption (void)
```

相关声明：[ztest_skip_failed_assumption](#a17537c79021fbc12e56b72ccec4b99c5)。

## 16.3\_详细说明（Detailed Documentation）

<a id="a06a081e3d716be7e024973cbf305c14b"></a>

### `ztest_relative_filename()`

```c
const char * ztest_relative_filename ( const char * file)
```

<a id="a17537c79021fbc12e56b72ccec4b99c5"></a>

### `ztest_skip_failed_assumption()`

```c
void ztest_skip_failed_assumption ( void )
```

<a id="a5c6bb493c88f7426a827889526dc0772"></a>

### `ztest_test_expect_fail()`

```c
void ztest_test_expect_fail ( void )
```

<a id="acd6eb423f54dce8544f7c3b1618c0374"></a>

### `ztest_test_fail()`

```c
void ztest_test_fail ( void )
```

<a id="ada3b1fcfa71db1bf7787c03ff45256d5"></a>

### `ztest_test_skip()`

```c
void ztest_test_skip ( void )
```


## 16.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdio.h](../api_source_system_reference/P042_stdio.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/tc_util.h](../api_source_architecture_reference/P021_tc_util.h_源码浏览.md)
- [zephyr/ztest.h](../api_source_configuration_reference/P127_ztest.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P057_ztest_assert.h_源码浏览.md)
- [zassert](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga0911ad9e94cdf1fe011d21316683ee7f)
- [zassume](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga5a4319eec770be532f34acb86e022c48)
- [zexpect](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga7bd837a8164123e3a06795b9f87a308d)
- [zassert_unreachable](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga300684a6b56e73e2cad6fd7458541129)
- [zassert_true](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gaeebddde19012223e3d5e853a1dac3ac5)
- [zassert_false](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga7330d1794fb961e07ee40294019dead0)
- [zassert_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gade40e2ec78ec813739e7725524fae7f0)
- [zassert_not_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gafe0e2609f77906ab0caddc31448a4fc8)
- [zassert_is_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gac0839891fd8bb7313b98551465e04c19)
- [zassert_not_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga849adad4afe893a7ae3dc2fbe750dc00)
- [zassert_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gacd075c7ee4dc2d64701bd3098a31b673)
- [zassert_not_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga43f306bf33d5e837b8927df16b82a363)
- [zassert_equal_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gabf20273fcba9cc45939a9f7db77f0bfc)
- [zassert_within](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gacc930af1a66e8533c5eca9526e198b4b)
- [zassert_between_inclusive](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga2b6b41de3e4856b21458febab3261b91)
- [zassert_mem_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gabbfcf6345172387326d35b5d0e2bb051)
- [zassert_mem_equal__](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga30e5fefa185944d3e949d4023c2eea27)
- [zassert_str_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga382017945a8c409e885cad8d0909b197)
- [zassume_true](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga6f5778ed8c1205126f7dcafb6eb26905)
- [zassume_false](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga5acf4256e5af3afaed06da7400dc3ad5)
- [zassume_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga9c6d1c701dd2d50027bf5e24b7567ae4)
- [zassume_not_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga539831d2f42cc991a8295b388ec12846)
- [zassume_is_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga3c5b1814deb5974e8ba0af961b516fa0)
- [zassume_not_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga24f4144edf5cef493c88872c7d56900e)
- [zassume_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga88c2a3153568a6f621b88dd6ceeb48d6)
- [zassume_not_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga0d90bb874c3135ffee870a4b61607853)
- [zassume_equal_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga78d6fbbf5eb13b32a5164053811b6cca)
- [zassume_within](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gad808c91e07e6c27b2e28ec7e04e03854)
- [zassume_between_inclusive](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gacff02eeba8dd334b3727dbe2036617e3)
- [zassume_mem_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga62be45256399530167745e71226e4a37)
- [zassume_mem_equal__](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gaaed6045f194ead4ffe1dd72a6fa5175d)
- [zassume_str_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga33a9cd37d321f1a421a1328e67b04788)
- [zexpect_true](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaef66b2764b6086dfbe8cbc933a8cfdc3)
- [zexpect_false](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga619bd320e39799414383a228dc2d8299)
- [zexpect_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaab325ee22058252c6a1c3243f3226657)
- [zexpect_not_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gabde5406775f05d5fcd135eb926969004)
- [zexpect_is_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga10b2c904f1c68b816eae2ad53e2b9f90)
- [zexpect_not_null](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaa51053fe2a07c6417db7952d7a594798)
- [zexpect_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga5ba65dbf95c204ed60694c5757db247f)
- [zexpect_not_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga31d83ab89828a03aebe0d0dc003f5232)
- [zexpect_equal_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gabf791d13c5781fc2215289d6dd925b3e)
- [zexpect_within](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga907afb07269bbc444a3d8ffee46839b5)
- [zexpect_between_inclusive](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gac37ebea6a9c71e3666a4911ceea5c913)
- [zexpect_mem_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaee52264e5f92a606a2a85f5fbb0a85fb)
- [zexpect_str_equal](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gacd5ef284610ca2027fc2e892243dfd38)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_zephyr__dt-bindings__pinctrl__tiva-c-pinctrl.h_文件参考.md) · [返回大纲](大纲.md)
