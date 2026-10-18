---
id: learning.zephyr-docs.testing.test-ztest
title: Ztest测试框架
kind: reference
status: maintained
domains: [zephyr, testing]
source_url: https://docs.zephyrproject.org/latest/develop/test/ztest.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="test-framework"></a>

# 第2章\_Ztest测试框架

原文：[Test Framework](https://docs.zephyrproject.org/latest/develop/test/ztest.html)。读取日期：2026-10-12，`latest`。

**Zephyr测试框架（Zephyr Test Framework，Ztest）**面向开发阶段，提供基本**断言（Assertion）**宏与通用测试结构。它既可用于**集成测试（Integration Testing）**，也可对特定模块开展**单元测试（Unit Testing）**。

## 2.1\_集成测试快速开始

官方可用基础示例位于 [samples/subsys/testsuite/integration](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/testsuite/integration)。若要测试名为 `foo` 的模块中名为 `bar` 的组件，可复制示例目录到 `tests/foo/bar`，再按被测应用目的编辑其中的文件；这两个名字是示例占位名称。

在 Zephyr 源码根目录，用 **Twister（Zephyr测试运行器）**构建并执行测试应用中适用的**测试场景（Test Scenario）**：

```sh
west twister -T tests/foo/bar/
```

只选择一个场景时使用 `--scenario`：

```sh
west twister --scenario tests/foo/bar/your.test.scenario.name
```

其中 `tests/foo/bar` 是测试应用目录，`your.test.scenario.name` 是该应用 `tests.yaml` 中声明的场景名，对应基础示例的 `sample.testing.ztest`。Twister 如何处理 Ztest 应用，见[测试项目关系图](https://docs.zephyrproject.org/latest/develop/twister/index.html#twister-test-project-diagram)。

> 译注：这些路径和名称用于说明如何建立自己的测试应用，不是本译文已经创建的测试工程。下面四个文件完整保留官方示例代码，移除了网页显示用的行号标记。

### 2.1.1\_基础示例文件

`CMakeLists.txt` 发现 Zephyr 包、建立应用，并把 `src/*.c` 加入名为 `app` 的应用构建目标。

> 译注：下例的 CMake 参数 `VERSION` 指定最低版本；`REQUIRED` 表示找不到包即报错；`HINTS` 给出搜索提示，`$ENV{ZEPHYR_BASE}` 读取指向 Zephyr 源码根的环境变量。命令 `FILE` 的 `GLOB` 模式匹配源文件，`PRIVATE` 将这些源文件加入当前目标。这些是构建语法，不是需自行定义的测试选项。

```cmake
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.28.0)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(integration)

FILE(GLOB app_sources src/*.c)
target_sources(app PRIVATE ${app_sources})
```

`tests.yaml` 声明场景、平台和标签：

```yaml
tests:
  # section.subsection
  sample.testing.ztest:
    build_only: true
    platform_allow:
      - native_sim
    integration_platforms:
      - native_sim
    tags: test_framework
```

> 译注：本原例设置了 `build_only: true`，所以直接按这一配置运行 Twister 只验证构建，并不会执行设备端用例。要执行测试，需要按实际场景调整这一设置，不能把上述概括的“构建并执行”当成当前 YAML 已经执行成功。`native_sim` 是主机原生模拟目标。

`prj.conf` 启用 Kconfig 选项 `CONFIG_ZTEST`：

```kconfig
CONFIG_ZTEST=y
```

`src/main.c` 用宏 `ZTEST_SUITE` 声明名为 `framework_tests` 的**测试套件（Test Suite）**，再用宏 `ZTEST` 加入一个验证多种断言的**测试用例（Test Case）**：

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/ztest.h>


ZTEST_SUITE(framework_tests, NULL, NULL, NULL, NULL, NULL);

/**
 * @brief Test Asserts
 *
 * This test verifies various assert macros provided by ztest.
 *
 */
ZTEST(framework_tests, test_assert)
{
	zassert_true(1, "1 was false");
	zassert_false(0, "0 was true");
	zassert_is_null(NULL, "NULL was not NULL");
	zassert_not_null("foo", "\"foo\" was NULL");
	zassert_equal(1, 1, "1 was not equal to 1");
	zassert_equal_ptr(NULL, NULL, "NULL was not equal to NULL");
}
```

一个测试应用可以包含多个套件，分别测试功能或 **应用程序编程接口（Application Programming Interface，API）**。用例函数遵循以下规则：名称以 `test_` 开头；通过 **Doxygen（源码注释文档生成工具）**说明用途；在所属测试分类或组件内名称唯一。

例如：

```c
/**
 * @brief Test Asserts
 *
 * This test case verifies the zassert_true macro.
 */
ZTEST(my_suite, test_assert)
{
        zassert_true(1, "1 was false");
}
```

### 2.1.2\_列出用例

Zephyr 测试应用包含多个围绕某种 API 或功能的场景。Twister 可解析全部或选定应用中的场景、套件和用例，并逐用例报告通过、失败、受阻或跳过。

它从源文件解析用例名称。例如列出内核测试：

```sh
west twister --list-tests -T tests/kernel
```

### 2.1.3\_显式跳过

特定架构或平台专属测试不能在所有目标上运行，但仍应计入清单并报告跳过。因为用例清单来自源码，靠条件编译让整个用例消失并不理想。

需要按平台或功能跳过时，显式调用 `ztest_test_skip()` 或宏 `Z_TEST_SKIP_IFDEF`；实际运行的测试则报告通过或失败。例如，下面用测试自定的 Kconfig 条件 `CONFIG_TEST1`、`CONFIG_BUGxxxxx` 决定是否跳过：

```c
#ifdef CONFIG_TEST1
ZTEST(common, test_test1)
{
     zassert_true(1, "true");
}
#else
ZTEST(common, test_test1)
{
     ztest_test_skip();
}
#endif

ZTEST(common, test_test2)
{
     Z_TEST_SKIP_IFDEF(CONFIG_BUGxxxxx);
     zassert_equal(1, 0, NULL);
}

ZTEST_SUITE(common, NULL, NULL, NULL, NULL, NULL);
```

> 译注：`CONFIG_TEST1` 和 `CONFIG_BUGxxxxx` 是原例条件名，需要由实际测试定义。第二个断言在没有跳过时故意比较 `1` 与 `0`，预期会失败，并非可用于验证相等行为的成功用例。

## 2.2\_单元测试快速开始

Ztest 单元测试可只编译特定模块并直接调用被测函数，从而避免为了测一个函数而构建整个 Zephyr 操作系统，加快构建与运行。

在单元测试源文件目录添加 `CMakeLists.txt`、`tests.yaml` 和 `prj.conf`，使用 `-DBOARD=unit_testing` 构建。Twister 的 `scripts/pylib/twister/twisterlib/testplan.py` 在这种板目标下只选择 `type: unit` 的场景。

> 原文注意：单元测试作为主机原生应用运行，受[POSIX架构限制](../native_reference/P002_POSIX架构.md#posix-arch-limitations)约束，仅支持 Linux。在 Windows 或 macOS 上需使用运行 Linux 的容器或虚拟机，并按[POSIX架构依赖说明](../native_reference/P002_POSIX架构.md#posix-arch-deps)准备环境。

### 2.2.1\_unit_testing伪开发板

官方 [unit_testing](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/boards/unit_testing) 位于 `subsys/testsuite/boards/unit_testing`。它既不是真实硬件，也不是模拟目标，而是 `arch: unit` 的**伪开发板（Pseudo-board）**：使用主机工具链生成普通原生可执行文件。

Twister 对 `type: unit` 场景自动选择它。构建只链接加入 `testbinary` 目标的源文件与 Ztest **测试支撑程序（Test Harness）**，不构建 Zephyr 内核或操作系统。因此没有启动流程、调度器、设备树驱动的设备初始化或驱动模型。

被测模块依赖的内核 API 或其他对象，必须由测试提供，通常采用**桩函数（Stub）**或**模拟对象（Mock）**。

### 2.2.2\_与native_sim的区别

| 目标 | 构建和运行内容 | 测试用途 |
| --- | --- | --- |
| [native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) | 将完整 Zephyr 内核、设备树、Kconfig、驱动与子系统编译成主机可执行文件，按 Zephyr 镜像启动运行。 | 在运行中的 Zephyr 系统上下文测试完整应用或集成功能，不设置 `type: unit`。 |
| `unit_testing` | 只链接被测代码与 Ztest，其余依赖由桩或模拟提供，直接调用函数。 | 隔离单个模块，必须设置 `type: unit`；速度快，但需要自行提供依赖。 |

> 译注：**可移植操作系统接口（Portable Operating System Interface，POSIX）**是本节主机架构名称所涉及的标准接口体系。两种目标都运行在主机上，并不表示具有同一套 Zephyr 运行环境。

### 2.2.3\_单元测试文件

`CMakeLists.txt` 从 [unittest组件](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/modules/unittest.cmake)取得 `testbinary` 目标，并加入相关源文件；`find_package` 的 `COMPONENTS unittest` 参数指定仅请求该组件：

```cmake
cmake_minimum_required(VERSION 3.28.0)

project(app)
find_package(Zephyr COMPONENTS unittest REQUIRED HINTS $ENV{ZEPHYR_BASE})
target_sources(testbinary PRIVATE main.c)
```

因为没有包含常用内核数据结构及其实现，测试必须补充依赖桩。Ztest 提供函数模拟辅助机制。Mock 可模拟复杂对象，并检查交互是否发生，必要时还检查交互顺序，以判断测试结果。

`tests.yaml` 的 `type` 必须为 `unit`：

```yaml
tests:
   testscenario.testsuite:
      tags: your_tag
      type: unit
```

`prj.conf` 通常只需：

```kconfig
CONFIG_ZTEST=y
```

如需数学库等额外库，可在 `CMakeLists.txt` 或 `tests.yaml` 中添加。例如传入链接参数 `-lm`：

```yaml
tests:
   testscenario.testsuite:
      tags: your_tag
      type: unit
      extra_args:
         - EXTRA_LDFLAGS="-lm"
```

更多例子见官方 [tests/unit/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/unit/)。

## 2.3\_创建套件

宏 `ZTEST_SUITE` 按以下顺序接受六个参数：

| 参数或回调类型 | 作用 |
| --- | --- |
| `suite_name` | 套件名称，在一个测试二进制中必须唯一。 |
| `ztest_suite_predicate_t` | 可选**谓词（Predicate）**，收到 `ztest_run_all()` 传入的全局状态指针，返回布尔值决定是否运行套件。 |
| `ztest_suite_setup_t` | 可选**套件准备函数（Setup）**，每次套件运行调用一次，返回测试夹具。 |
| `ztest_suite_before_t` | 可选**用例前置函数（Before）**，每个用例之前调用。 |
| `ztest_suite_after_t` | 可选**用例后置函数（After）**，每个用例之后调用。 |
| `ztest_suite_teardown_t` | 可选**套件清理函数（Teardown）**，套件全部用例结束时调用。 |

带谓词的例子：

```c
#include <zephyr/ztest.h>
#include "test_state.h"

static bool predicate(const void *global_state)
{
     return ((const struct test_state*)global_state)->x == 5;
}

ZTEST_SUITE(alternating_suite, predicate, NULL, NULL, NULL, NULL);
```

> 译注：`test_state.h` 及其中 `struct test_state` 由测试作者提供；本例要求全局状态指针有效，并在 `x == 5` 时运行套件。`NULL` 表示没有相应可选回调。

## 2.4\_添加用例与测试夹具

原文列出五个添加用例的宏。其中 Kconfig 选项 `CONFIG_USERSPACE` 控制**用户空间（User Space）**支持，用于让指定测试在受权限限制的用户态线程中运行：

| 宏 | 行为 |
| --- | --- |
| `ZTEST(suite_name, test_name)` | 将指定用例加入指定套件。 |
| `ZTEST_P(suite_name, test_name)` | 添加**值参数化测试（Value-parameterized Test）**，按注册参数逐值执行，参数与套件夹具互不覆盖。 |
| `ZTEST_USER(suite_name, test_name)` | 类似 `ZTEST`；启用 `CONFIG_USERSPACE` 时在用户态线程运行。 |
| `ZTEST_F(suite_name, test_name)` | 类似 `ZTEST`，并提供名为 `fixture`、类型对应 `<suite_name>_fixture` 的变量。 |
| `ZTEST_USER_F(suite_name, test_name)` | 同时提供夹具变量与用户态线程行为。 |

**测试夹具（Test Fixture）**用于共享重复的准备工作。同一套件的多个测试常需一次初始准备，并在每次测试之间复位状态。例如：

```c
#include <zephyr/ztest.h>

struct my_suite_fixture {
     size_t max_size;
     size_t size;
     uint8_t buff[1];
};

static void *my_suite_setup(void)
{
     /* Allocate the fixture with 256 byte buffer */
     struct my_suite_fixture *fixture = malloc(sizeof(struct my_suite_fixture) + 255);

     zassume_not_null(fixture, NULL);
     fixture->max_size = 256;

     return fixture;
}

static void my_suite_before(void *f)
{
     struct my_suite_fixture *fixture = (struct my_suite_fixture *)f;
     memset(fixture->buff, 0, fixture->max_size);
     fixture->size = 0;
}

static void my_suite_teardown(void *f)
{
     free(f);
}

ZTEST_SUITE(my_suite, NULL, my_suite_setup, my_suite_before, NULL, my_suite_teardown);

ZTEST_F(my_suite, test_feature_x)
{
     zassert_equal(0, fixture->size);
     zassert_equal(256, fixture->max_size);
}
```

此例先分配含256字节缓冲区的夹具，每个用例前清零缓冲区和长度，套件结束后释放。`zassume_not_null()` 验证分配前提。

在 `ZTEST_USER` 或 `ZTEST_USER_F` 等用户态线程中使用夹具分配的内存时，必须声明该内存可被用户空间访问，因为它由内核空间拥有并初始化。框架提供 `ZTEST_DMEM` 与 `ZTEST_BMEM` 宏标记内核和用户空间共享的测试数据。

## 2.5\_值参数化测试

一份测试主体可对给定列表中的每个值各执行一次，类似 **GoogleTest（C++测试框架）**的 `TEST_P` / `INSTANTIATE_TEST_SUITE_P` 模式。

套件准备函数 `setup()` 返回的夹具始终通过 `data` 传入，不会被当前参数替换。参数另通过运行时访问接口取得。

### 2.5.1\_测试主体

用 `ZTEST_P` 定义主体，从 `data` 取得夹具，通过 `ZTEST_GET_PARAM(int)` 取得本次整数参数：

```c
#include <zephyr/ztest.h>

struct my_suite_fixture {
     int initial_value;
};

static void *my_suite_setup(void) {
     static struct my_suite_fixture f = { .initial_value = 42 };
     return &f;
}

ZTEST_SUITE(my_suite, NULL, my_suite_setup, NULL, NULL, NULL);

ZTEST_P(my_suite, test_multiply)
{
     struct my_suite_fixture *f = (struct my_suite_fixture *)data;
     int factor = ZTEST_GET_PARAM(int);

     /* fixture is always intact, regardless of parameter */
     zassert_equal(f->initial_value, 42, "fixture corrupted");
     zassert_true(f->initial_value * factor > 0, "product must be positive");
}
```

本例检查夹具初始值始终为42，并检查乘积大于0。

### 2.5.2\_参数值集合

`ZTEST_DEFINE_PARAM_VALUES` 从字面值建立静态集合：

```c
ZTEST_DEFINE_PARAM_VALUES(small_factors, int, 1, 2, 3);
```

已有数组时使用宏 `ZTEST_DEFINE_PARAM_VALUES_ARRAY`，从数组建立参数集合：

```c
static const int big_factors[] = { 10, 100, 1000 };
ZTEST_DEFINE_PARAM_VALUES_ARRAY(big_factor_vals, big_factors);
```

数值范围使用宏 `ZTEST_DEFINE_PARAM_RANGE`，语义类似 GoogleTest 的 `testing::Range(begin, end [, step])`；参数 `begin` 是起点，`end` 是不包含的终点，`step` 是步长，依次产生 `begin`、`begin+step` 等值：

```c
/* {0, 2, 4, 6, 8} — 5 values, step is supplied explicitly */
ZTEST_DEFINE_PARAM_RANGE(even_vals, int, 0, 10, 2);

/* {1, 2, 3, 4, 5} — step=1 is the common case */
ZTEST_DEFINE_PARAM_RANGE(one_to_five, int, 1, 6, 1);
```

范围不分配保存全部值的后备数组，因此不会因范围增大而增加这类 **随机存取存储器（Random-Access Memory，RAM）**占用。宏要求 `end > begin` 且 `step > 0`，通过 `BUILD_ASSERT` 在编译时检查。

参数若需运行时计算，例如随机数、传感器读数或算法结果，可使用 `ZTEST_DEFINE_PARAM_GENERATOR` 或 `ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP`。二者都接受用户提供的**生成器（Generator）**回调 `void gen(size_t index, void *out)`，每次写入一个值，也不分配后备数组。

带 `_WITH_SETUP` 的版本在分发循环前额外调用一次 `void setup(void)` 钩子，可初始化**伪随机数生成器（Pseudo-Random Number Generator，PRNG）**种子、复位有状态计数器或打开所需资源：

> 译注：代码注释中的 **随机数生成器（Random Number Generator，RNG）**是上述 PRNG 所属的通用类别。`MY_FUZZ_SEED`、`MY_FUZZ_ITERATIONS` 是测试自定的种子与迭代次数常量；`ARG_UNUSED` 宏标明参数不使用，以避免编译告警。

```c
#include <zephyr/random/random.h>

/* Seed the RNG before the first iteration so failures are reproducible. */
static void seed_rng(void)
{
     sys_rand_seed(MY_FUZZ_SEED);
}

static void rand_u32_gen(size_t idx, void *out)
{
     ARG_UNUSED(idx);
     *(uint32_t *)out = sys_rand32_get();
}

ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP(fuzz_vals, uint32_t, MY_FUZZ_ITERATIONS,
                                        seed_rng, rand_u32_gen);
```

> 译注：`MY_FUZZ_SEED`、`MY_FUZZ_ITERATIONS` 是测试自定常量。原例的 `sys_rand_seed()` 在本仓库 `zephyr/random/random.h` 中没有公开声明，不能把它当作所有版本均提供的通用种子接口；需按实际随机后端提供可复现的初始化方法。原代码保留供对照。

不需准备函数时使用较简单的形式：

```c
static void deterministic_gen(size_t idx, void *out)
{
     /* Deterministic but computed at runtime (e.g. based on hardware ID). */
     *(uint32_t *)out = get_device_seed() ^ (uint32_t)idx;
}

ZTEST_DEFINE_PARAM_GENERATOR(hw_vals, uint32_t, 16U, deterministic_gen);
```

这里的 `get_device_seed()` 同样由测试提供。两种生成器宏的 `count_` 必须是常量表达式，如数值字面量、宏或相应配置常量，不支持真正运行时变化的参数数量。

结构体参数采用相同机制；宏 `ZTEST_GET_PARAM_PTR(struct point)` 返回当前点参数的只读指针：

```c
struct point { int x; int y; };

static const struct point corners[] = { {0,0}, {1,0}, {0,1}, {1,1} };
ZTEST_DEFINE_PARAM_VALUES_ARRAY(corner_vals, corners);

ZTEST_P(my_suite, test_in_unit_square)
{
     const struct point *p = ZTEST_GET_PARAM_PTR(struct point);
     zassert_true(p->x >= 0 && p->x <= 1 && p->y >= 0 && p->y <= 1,
                 "point (%d, %d) outside unit square", p->x, p->y);
}
```

`ZTEST_GET_PARAM_PTR(struct point)` 取得当前点的只读指针，例中验证点位于单位正方形内。

### 2.5.3\_实例化

`ZTEST_INSTANTIATE_TEST_SUITE_P` 将值集合绑定到测试主体。同一主体可用不同集合多次实例化：

```c
ZTEST_INSTANTIATE_TEST_SUITE_P(small, my_suite, test_multiply, small_factors);
ZTEST_INSTANTIATE_TEST_SUITE_P(big,   my_suite, test_multiply, big_factor_vals);
```

第一个参数 `small` / `big` 是编译单元内唯一的自定标识，记录在测试元数据中，不改变 Twister 报告的测试命名。

### 2.5.4\_读取当前参数

| 辅助接口 | 返回内容 |
| --- | --- |
| `ztest_has_current_param()` | 在参数化调用中返回 `true`。 |
| `ztest_get_current_param()` | 指向当前值的 `const void *`。 |
| `ZTEST_GET_PARAM_PTR(type)` | 指向当前值的 `const type *`。 |
| `ZTEST_GET_PARAM(type)` | 解引用并以 `type` 取得当前值。 |
| `ztest_get_current_param_index()` | 当前值在集合中从0开始的索引。 |
| `ztest_get_current_param_size()` | 单个参数元素的字节数。 |

非参数化的 `ZTEST`、`ZTEST_F` 中，前两个接口分别返回 `false` 与 `NULL`。

## 2.6\_结果预期与通用规则

除了测试主体，框架还能声明预期结果，并在所有测试前后执行共同规则。前者改变结果判定，后者组织重复的准备与清理工作。

### 2.6.1\_预期失败或跳过

某些测试本来就应触发失败或跳过。可用宏 `ZTEST_EXPECT_FAIL` 或 `ZTEST_EXPECT_SKIP` 分别标明预期失败、预期跳过：

```c
#include <zephyr/ztest.h>

ZTEST_SUITE(my_suite, NULL, NULL, NULL, NULL, NULL);

ZTEST_EXPECT_FAIL(my_suite, test_fail);
ZTEST(my_suite, test_fail)
{
  /** This will fail the test */
  zassert_true(false, NULL);
}

ZTEST_EXPECT_SKIP(my_suite, test_skip);
ZTEST(my_suite, test_skip)
{
  /** This will skip the test */
  zassume_true(false, NULL);
}
```

如果没有预期声明，两个用例分别会被判为失败和跳过。存在相应声明时，因为实际结果符合预期，Ztest 将它们标为通过。

### 2.6.2\_测试规则

**测试规则（Test Rule）**可以对每个套件的每个测试执行共同逻辑，与当前运行哪个套件无关。例如复位 Mock、模拟器状态，或清理 **通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）**数据。

下面使用 **假函数框架（Fake Function Framework，FFF）**及 `ZTEST_RULE`，在用例之前复位假函数调用状态：

> 译注：`DEFINE_FFF_GLOBALS` 宏定义 FFF 全局状态，`RESET_FAKE` 宏复位指定假函数的记录。原文的 `DEFINE_FAKE_VOID_FUN` 意图定义无返回值假函数，但拼写缺少末尾的 `C`，详见代码后的修正说明。

```c
#include <zephyr/fff.h>
#include <zephyr/ztest.h>

#include "test_mocks.h"

DEFINE_FFF_GLOBALS;

DEFINE_FAKE_VOID_FUN(my_weak_func);

static void fff_reset_rule_before(const struct ztest_unit_test *test, void *fixture)
{
     ARG_UNUSED(test);
     ARG_UNUSED(fixture);

     RESET_FAKE(my_weak_func);
}

ZTEST_RULE(fff_reset_rule, fff_reset_rule_before, NULL);
```

> 译注：`test_mocks.h` 和 `my_weak_func` 由测试提供。原例写成 `DEFINE_FAKE_VOID_FUN`，本仓库 FFF 头文件公开的相应宏是 `DEFINE_FAKE_VOID_FUNC`，末尾多一个 `C`；后者用于与已有声明配合定义假函数。若没有预先声明，则需按 FFF 接口选择完整的声明与定义组合，不能只照抄拼写有误的宏。

## 2.7\_自定义test_main

Ztest 提供默认测试入口函数 `test_main()`，但应用可以自定义。当测试依赖无法方便复制、或必须重启进程才能复现的全局状态时，这尤其有用。例如开发板有多个上电阶段，套件可通过谓词选择自己应运行的阶段；下面的 `PWR_PHASE_0`、`PWR_PHASE_1`、`PWR_PHASE_2` 是测试自定的三个阶段常量：

```c
#include <zephyr/ztest.h>

#include "my_test.h"

void test_main(void)
{
     struct power_sequence_state state;

     /* Only suites that use a predicate checking for phase == PWR_PHASE_0 will run. */
     state.phase = PWR_PHASE_0;
     ztest_run_all(&state, false, 1, 1);

     /* Only suites that use a predicate checking for phase == PWR_PHASE_1 will run. */
     state.phase = PWR_PHASE_1;
     ztest_run_all(&state, false, 1, 1);

     /* Only suites that use a predicate checking for phase == PWR_PHASE_2 will run. */
     state.phase = PWR_PHASE_2;
     ztest_run_all(&state, false, 1, 1);

     /* Check that all the suites in this binary ran at least once. */
     ztest_verify_all_test_suites_ran();
}
```

`my_test.h`、电源状态结构体和阶段常量由测试定义。每次 `ztest_run_all()` 执行匹配当前状态的套件；最后的 `ztest_verify_all_test_suites_ran()` 检查该二进制中的全部套件是否至少执行过一次。

接口为 `ztest_run_all(const void *state, bool shuffle, int suite_iter, int case_iter)`；随机顺序需要启用 Kconfig 选项 `CONFIG_ZTEST_SHUFFLE`：

| 参数 | 作用 |
| --- | --- |
| `state` | 传给各套件谓词的全局状态指针。 |
| `shuffle` | 为 `true` 时随机化套件及用例顺序，需要 `CONFIG_ZTEST_SHUFFLE`；为 `false` 时保持默认字母数字顺序。 |
| `suite_iter` | 每个套件重复次数。 |
| `case_iter` | 每个用例重复次数。 |

原例每次只运行匹配套件一遍，不打乱顺序。

## 2.8\_声明套件的最佳实践

Twister 和其他验证工具需要知道一个 Ztest 镜像将提供哪些用例，这是为了**可追溯性（Traceability）**。仅有一个“信号量测试应用”名称还不够；还需要显示各 API 和功能对应的测试点，并关联接口文档和功能要求。

报告应逐用例显示通过、失败、受阻或跳过。特别是一个测试应用做很多事情时，只报告应用总体结果过于笼统。

原文解释了两种未采用方式：

- 不只依赖 **C预处理器（C Preprocessor，CPP）**输出或构建后的 **可执行与可链接格式（Executable and Linkable Format，ELF）**文件来扫描用例，因为一旦预处理或构建失败，就无法识别内部用例。
- 不把全部用例名称另行复制到 YAML 配置中，因为独立描述文件增加维护和重复信息。把名称保留在测试源文件中，只需随实现修改一处。

## 2.9\_Ztress压力测试

**Zephyr压力测试框架（Zephyr Stress Test Framework，Ztress）**在多个优先级上下文执行用户函数，用来检验代码能否承受**抢占（Preemption）**。它为各上下文跟踪执行和被抢占次数，并可按超时、执行次数或抢占次数结束。

框架创建所需数量、不同优先级的线程，可选地启动定时器。每个上下文调用自己的用户函数，然后休眠随机数量的**系统时钟节拍（System Tick）**。框架跟踪 **中央处理器（Central Processing Unit，CPU）**负载，并调整休眠时间以提高负载。

为增加抢占概率，系统时钟频率应较高。原文指出 QEMU x86 默认100 Hz过低，建议提高到100 kHz。

> 译注：这是针对该压力测试环境的原文建议，不是本项目硬件应直接采用的频率；实际时钟源、定时能力和中断开销仍需另行核对。

### 2.9.1\_执行与结束条件

`ZTRESS_EXECUTE` 接受可变数量的上下文参数，分别由 `ZTRESS_TIMER` 或 `ZTRESS_THREAD` 宏描述，按优先级从高到低排列。每个上下文指定最低执行次数和抢占次数；全部条件满足并完成后打印报告，宏才返回。运行期间还会定期打印进度。

也可通过 `ztress_set_timeout()` 限定超时，或调用 `ztress_abort()` 提前结束。用户函数收到执行计数以及“是否最后一次执行”的标志。

下面建立三个上下文，其中一个是 `k_timer` 的**中断服务程序（Interrupt Service Routine，ISR）**上下文。每个至少执行10000次，最低优先级上下文至少被抢占1000次；若10秒仍未满足则超时结束。每个上下文最后一个参数是初始休眠时间，框架会在运行中调整：

```c
ztress_set_timeout(K_MSEC(10000));
ZTRESS_EXECUTE(ZTRESS_TIMER(foo_0, user_data_0, 10000, Z_TIMEOUT_TICKS(20)),
               ZTRESS_THREAD(foo_1, user_data_1, 10000, 0, Z_TIMEOUT_TICKS(20)),
               ZTRESS_THREAD(foo_2, user_data_2, 10000, 1000, Z_TIMEOUT_TICKS(20)));
```

### 2.9.2\_静态配置

| Kconfig选项 | 含义 |
| --- | --- |
| [CONFIG_ZTRESS_MAX_THREADS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTRESS_MAX_THREADS) | 支持的线程数量。 |
| [CONFIG_ZTRESS_STACK_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTRESS_STACK_SIZE) | 创建的线程栈大小。 |
| [CONFIG_ZTRESS_REPORT_PROGRESS_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTRESS_REPORT_PROGRESS_MS) | 进度报告间隔。 |

## 2.10\_API分类与检查结果

运行测试的独立参考入口为 [Ztest测试宏](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html)。下面三类检查对失败的处理不同。

### 2.10.1\_断言

**断言（Assertion）**失败会立即使当前测试失败，并打印文件、行号、函数、失败原因及可选消息。Kconfig 选项 [CONFIG_ZTEST_ASSERT_VERBOSE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_ASSERT_VERBOSE) 为0时，只打印文件与行号，以缩小测试二进制。

例如 `zassert_equal(buf->ref, 2, "Invalid refcount")` 失败时输出：

```text
Assertion failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
Aborted at unit test function
```

完整接口见[断言宏](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html)。

### 2.10.2\_期望

**期望检查（Expectation）**失败后仍继续执行用例，到用例结束时再标记失败。失败时也打印文件、行号、函数、原因及可选消息；`CONFIG_ZTEST_ASSERT_VERBOSE=0` 时同样只打印文件和行号。

例如下面两次期望检查失败：

```c
zexpect_equal(buf->ref, 2, "Invalid refcount");
zexpect_equal(buf->ref, 1337, "Invalid refcount");
```

示意输出如下；其中 `START` 表示开始执行，`FAIL` 表示本用例最终失败：

```text
START - test_get_single_buffer
    Expectation failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
    Expectation failed at main.c:63: test_get_single_buffer: Invalid refcount (buf->ref not equal to 1337)
 FAIL - test_get_single_buffer in 0.0 seconds
```

完整接口见[期望宏](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html)。这里的 Expectation 检查与前文 `ZTEST_EXPECT_FAIL` 声明预期结果，属于不同用途。

### 2.10.3\_假设

**前提假设（Assumption）**不成立时立即跳过测试或套件，而不是判为失败。输出包含文件、行号、函数、原因和可选消息；关闭详细断言输出时只保留文件与行号。

例如 `zassume_equal(buf->ref, 2, "Invalid refcount")` 不成立：

```text
START - test_get_single_buffer
    Assumption failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
 SKIP - test_get_single_buffer in 0.0 seconds
```

完整接口见[假设宏](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html)。压力测试的独立 API 见 [Ztress宏](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html)。

### 2.10.4\_通过FFF提供替身

Zephyr 集成 [FFF](https://github.com/meekrosoft/fff) 用于模拟函数，使用时包含：

```c
#include <zephyr/fff.h>
```

Zephyr 还提供多个基于 FFF 的**假驱动（Fake Driver）**，可作为 Stub 或 Mock。实例通过设备树与 Kconfig 配置；原文列出以下绑定：

| 绑定 | 目标设备类型 |
| --- | --- |
| [zephyr,fake-can](https://docs.zephyrproject.org/latest/build/dts/api/bindings/can/zephyr%2Cfake-can.html#std-dtcompatible-zephyr-fake-can) | 控制器局域网（Controller Area Network，CAN）。 |
| [zephyr,fake-comp](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/zephyr%2Cfake-comp.html#std-dtcompatible-zephyr-fake-comp) | 比较器（Comparator）。 |
| [zephyr,fake-eeprom](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/zephyr%2Cfake-eeprom.html#std-dtcompatible-zephyr-fake-eeprom) | 电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）。 |
| [zephyr,fake-leds](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/zephyr%2Cfake-leds.html#std-dtcompatible-zephyr-fake-leds) | 发光二极管（Light-Emitting Diode，LED）。 |
| [zephyr,fake-pwm](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pwm/zephyr%2Cfake-pwm.html#std-dtcompatible-zephyr-fake-pwm) | 脉宽调制（Pulse-Width Modulation，PWM）。 |
| [zephyr,fake-regulator](https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/zephyr%2Cfake-regulator.html#std-dtcompatible-zephyr-fake-regulator) | 稳压器（Regulator）。 |
| [zephyr,fake-rtc](https://docs.zephyrproject.org/latest/build/dts/api/bindings/rtc/zephyr%2Cfake-rtc.html#std-dtcompatible-zephyr-fake-rtc) | 实时时钟（Real-Time Clock，RTC）。 |
| [zephyr,fake-stepper-ctrl](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/zephyr%2Cfake-stepper-ctrl.html#std-dtcompatible-zephyr-fake-stepper-ctrl) | 步进电机控制器（Stepper Controller）。 |
| [zephyr,fake-stepper-driver](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/zephyr%2Cfake-stepper-driver.html#std-dtcompatible-zephyr-fake-stepper-driver) | 步进电机驱动器（Stepper Driver）。 |

Zephyr 还提供简化假函数声明的 FFF 扩展，见章末入口。

## 2.11\_自定义测试输出

启用 Kconfig 选项 [CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE)，并创建 `tc_util_user_override.h` 提供覆盖定义。在项目 `CMakeLists.txt` 加入 `zephyr_include_directories(my_folder)`，让构建系统找到该头文件所在目录。

可覆盖哪些宏，见官方 [subsys/testsuite/include/zephyr/tc_util.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/include/zephyr/tc_util.h)。可替换的默认定义通常采用以下保护形式：

```c
#ifndef SOMETHING
#define SOMETHING <default implementation>
#endif /* SOMETHING */
```

> 译注：`my_folder`、`SOMETHING` 和 `<default implementation>` 是位置或定义占位；维护者应按实际要覆盖的宏填写，不能把占位词当成 Ztest 已有配置。

## 2.12\_打乱顺序与重复运行

默认测试按字母数字顺序排列执行，这可能掩盖对前一个测试状态的依赖。启用 [CONFIG_ZTEST_SHUFFLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_SHUFFLE) 可随机化顺序，失败测试的输出会显示所用种子；原生模拟构建还可通过 Twister 的 `--seed` 参数指定种子。

默认每个测试执行一次。启用 Kconfig 选项 [CONFIG_ZTEST_REPEAT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_REPEAT) 可重复执行套件与用例，两个默认重复因子均为3，即每个套件执行3轮，每轮中每个用例执行3次。可分别通过 Kconfig 计数选项 [CONFIG_ZTEST_SUITE_REPEAT_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_SUITE_REPEAT_COUNT) 和 [CONFIG_ZTEST_TEST_REPEAT_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_TEST_REPEAT_COUNT) 修改。

## 2.13\_在原生模拟程序中选择测试

为原生模拟器构建的测试可通过可执行文件命令行列出或选择用例。`-test` 接受逗号分隔的 `suite::test` 列表，用例名可换成 `*` 以运行套件全部用例：

```sh
$ zephyr.exe -list
$ zephyr.exe -test="fixture_tests::test_fixture_pointer,framework_tests::test_assert_mem_equal"
$ zephyr.exe -test="framework_tests::*"
```

> 译注：`$` 是原文提示符，不输入命令。`zephyr.exe` 指已生成的原生模拟程序，应从实际构建输出位置调用；这个文件名不表示上述仅支持 Linux 的测试已可在原生 Windows 上运行。

## 2.14\_FFF扩展参考

完整的独立接口入口为 [FFF Extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__fff__extensions.html)。本页保留原文所有 API 分类入口，独立生成的 Doxygen 页面仍按各自翻译状态处理。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：测试入口](P001_测试入口.md) · [本模块主线目录](../reading/testing.md) · [全部主线](../reading/README.md) · [下一篇：测试覆盖率](P003_测试覆盖率.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：测试入口](P001_测试入口.md) · [下一章：测试覆盖率](P003_测试覆盖率.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
