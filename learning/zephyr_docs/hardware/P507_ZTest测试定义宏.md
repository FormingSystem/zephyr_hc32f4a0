---
id: learning.zephyr-docs.hardware.ztestmac-4
title: ZTest测试定义宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第507章\_ZTest测试定义宏

原文：[group__ztest__test](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html)。读取日期：2026-10-13，`latest`。

本模块通过宏和测试结构简化 **Zephyr 测试框架（Zephyr Testing Framework，ZTest）**的使用，包括注册测试、参数化运行、套件回调、用户态测试和执行结果控制。公开头文件为 `zephyr/ztest_test.h`，源码位置为 `subsys/testsuite/ztest/include/zephyr/ztest_test.h`。

> 译注：原页显示官方构建机的绝对头文件路径，这里使用公开包含名。官方示例中存在名称拼写和说明不一致处，均保留代码并在对应位置说明。

## 507.1\_测试对象与普通测试

**测试套件（Test Suite）**组织多个单元测试。**测试夹具（Test Fixture）**是套件准备函数返回、在测试中共享的数据；**值参数化测试（Value-Parameterized Test）**则让同一测试函数依次接收不同参数值。它的参数上下文与夹具是独立对象。

原页列出的数据结构如下，成员详情由各自参考页给出。

| 结构 | 官方说明译文 |
| --- | --- |
| [`ztest_expected_result_entry`](P509_测试预期结果记录.md) | 单条预期结果记录，允许测试失败或跳过后仍视为通过 |
| [`ztest_unit_test`](P510_单元测试记录结构.md) | 单元测试结构；原页没有概述说明 |
| [`ztest_param_values`](P511_测试参数集合结构.md) | 值参数化测试的参数值集合 |
| [`ztest_param_inst`](P512_参数化测试注册结构.md) | 将测试映射到参数值集合的注册记录 |
| [`ztest_suite_stats`](P513_测试套件统计结构.md) | 测试套件统计信息 |
| [`ztest_unit_test_stats`](P514_单元测试统计结构.md) | 单元测试统计结构；原页没有概述说明 |
| [`ztest_suite_node`](P515_测试套件节点结构.md) | 单个测试套件节点 |
| [`ztest_arch_api`](P516_测试架构后端接口.md) | 架构专用应用程序编程接口（Application Programming Interface，API）结构 |

[`ZTEST`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac25858f76ea667d07de422a3b489cb15) 创建并注册一个新单元测试，把它附加到名为 `suite` 的套件，`fn` 是要调用的测试函数。套件不必与该测试定义在同一个**编译单元（Compilation Unit）**。

```c
#define ZTEST(suite, fn)
```

```c
Z_ZTEST(suite, fn, 0)
```

下文保留所有官方宏展开。`Z_ZTEST`、`Z_ZTEST_F`、`Z_TEST_P` 是内部测试定义宏；`BUILD_ASSERT` 在编译时检查条件；[`STRUCT_SECTION_ITERABLE`](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f) 将记录放入可遍历的链接段；[`ARRAY_SIZE`](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a) 取得数组元素数；`STRINGIFY` 将标识符转成字符串，[`UTIL_CAT`](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d) 及 `##` 用于拼接标识。`NULL` 是空指针，`__VA_ARGS__` 代表可变参数。

## 507.2\_运行时生成参数值

[`ZTEST_DEFINE_PARAM_GENERATOR`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gadd987aba574bae91f6c627cb1998e82d) 声明一个运行时生成的参数集合。

```c
#define ZTEST_DEFINE_PARAM_GENERATOR(name_, type_, count_, gen_cb_)
```

每次调用测试时，`gen_cb_` 都会执行一次，接收从 `0` 开始的迭代索引及指向已对齐临时缓冲区的指针。它必须向缓冲区写入**恰好 `sizeof(type_)` 字节**。回调可以读取随机数、硬件寄存器、计算值等任意运行时状态。

参数值不会存进数组，因而迭代数量 `count_` 不会带来额外的数组**随机存取存储器（Random Access Memory，RAM）**开销。编译时检查 `sizeof(type_)` **不得超过 16 字节**。需要一次性初始化，例如设置**伪随机数生成器（Pseudorandom Number Generator，PRNG）**种子时，应使用下一种带准备函数的宏。

| 参数 | 含义 |
| --- | --- |
| `name_` | 所生成变量的标识符 |
| `type_` | 每个生成值的 C 类型 |
| `count_` | 调用次数，必须为常量表达式 |
| `gen_cb_` | 生成器回调，类型为 `void (*)(size_t index, void *out)` |

```c
BUILD_ASSERT(sizeof(type_) <= 16U,                                                   \
             "ZTEST_DEFINE_PARAM_GENERATOR: type too large for scratch buffer");     \
static const struct ztest_param_values name_ = {                                     \
        .values      = NULL,                                                         \
        .count       = (count_),                                                     \
        .elem_size   = sizeof(type_),                                                \
        .name_cb     = NULL,                                                         \
        .value_at_cb = (gen_cb_),                                                    \
        .setup_cb    = NULL,                                                         \
}
```

[`ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga86db43dc0e56f416e86ace064f3d40d2) 与上述宏相同，但还注册 `setup_cb_`，在分派循环的第一次迭代之前调用一次。可用它设置 PRNG 种子、重置有状态计数器，或完成每次测试运行在生成参数前需要的初始化。

```c
#define ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP(name_, type_, count_, setup_cb_, gen_cb_)
```

`name_`、`type_`、`count_`、`gen_cb_` 的含义及约束同前；`setup_cb_` 类型为 `void (*)(void)`，在迭代 `0` 之前调用一次。

```c
BUILD_ASSERT(sizeof(type_) <= 16U,                                                   \
             "ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP: type too large");             \
static const struct ztest_param_values name_ = {                                     \
        .values      = NULL,                                                         \
        .count       = (count_),                                                     \
        .elem_size   = sizeof(type_),                                                \
        .name_cb     = NULL,                                                         \
        .value_at_cb = (gen_cb_),                                                    \
        .setup_cb    = (setup_cb_),                                                  \
}
```

官方**模糊测试（Fuzz Testing）**示例使用固定种子生成可复现的随机值。`MY_FUZZ_SEED` 和 `MY_FUZZ_ITERATIONS` 是示例的种子及迭代次数配置占位；`seed_rng` 为种子设置函数，`rand_u32` 为 32 位值生成函数，`ARG_UNUSED` 标记未使用参数，`sys_rand_seed` 和 [`sys_rand32_get`](https://docs.zephyrproject.org/latest/doxygen/html/group__random__api.html#ga62cb24a6049b7aa9d03d66786e4a4db6) 保留为原示例中的随机数接口名称。

```c
static void seed_rng(void) { sys_rand_seed(MY_FUZZ_SEED); }
static void rand_u32(size_t idx, void *out)
{
    ARG_UNUSED(idx);
    *(uint32_t *)out = sys_rand32_get();
}
ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP(fuzz_vals, uint32_t,
                                        MY_FUZZ_ITERATIONS,
                                        seed_rng, rand_u32);
```

## 507.3\_范围、字面值与已有数组

[`ZTEST_DEFINE_PARAM_RANGE`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gae5100e9440a1bea86a7840c24300efa0) 为参数化测试声明数值范围，仿照 GoogleTest 的 `testing::Range(begin, end [, step])`。范围是**左闭右开区间（Half-Open Range）**：包含 `begin_`，按 `step_` 递增，不包含 `end_`。

```c
#define ZTEST_DEFINE_PARAM_RANGE(name_, type_, begin_, end_, step_)
```

值由生成的回调按需计算，不分配数组，因此任意大的范围都不增加值数组的 RAM 开销。编译时要求 `end_ > begin_`、`step_ > 0`，且 `sizeof(type_) <= 16` 字节。

| 参数 | 含义 |
| --- | --- |
| `name_` | 所生成变量的标识符 |
| `type_` | 标量 C 类型，例如 `int` 或 [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) |
| `begin_` | 包含在范围内的首值 |
| `end_` | 不包含在范围内的上界 |
| `step_` | 相邻值的增量；原文称默认值为 `1` |

```c
BUILD_ASSERT((end_) > (begin_), "ZTEST_DEFINE_PARAM_RANGE: end must be > begin"); \
BUILD_ASSERT((step_) > 0, "ZTEST_DEFINE_PARAM_RANGE: step must be > 0");          \
BUILD_ASSERT(sizeof(type_) <= 16U,                                                   \
             "ZTEST_DEFINE_PARAM_RANGE: type too large for scratch buffer");        \
static void z_ztest_range_value_at_##name_(size_t z_idx_, void *z_out_)             \
{                                                                                    \
        type_ z_val_ = (type_)(begin_) + (type_)(step_) * (type_)(z_idx_);         \
        *(type_ *)z_out_ = z_val_;                                                   \
}                                                                                    \
static const struct ztest_param_values name_ = {                                     \
        .values      = NULL,                                                         \
        .count       = (size_t)(((end_) - (begin_) - 1) / (step_) + 1),             \
        .elem_size   = sizeof(type_),                                                \
        .name_cb     = NULL,                                                         \
        .value_at_cb = z_ztest_range_value_at_##name_,                              \
        .setup_cb    = NULL,                                                         \
}
```

> 译注：原文称省略步长时默认 `1`，但本页给出的宏声明和展开要求五个参数，没有展示可省略参数的包装层。实际调用应按当前头文件确认；按本页签名应显式传入 `step_`。所谓不增加 RAM 是不分配参数值数组，仍存在固定的临时缓冲区和登记记录。

[`ZTEST_DEFINE_PARAM_VALUES`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga37db3f58e35fdf40096ebad3f55e68ef) 用提供的字面值创建命名的静态只读 `struct ztest_param_values`，结果名称可直接传给 [`ZTEST_INSTANTIATE_TEST_SUITE_P()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga98baeb865dcc55c1880fd2c6f8771ad3)。

```c
#define ZTEST_DEFINE_PARAM_VALUES(name_, type_, ...)
```

`name_` 是变量标识符，`type_` 为每个参数值的 C 类型，`...` 为以逗号分隔的参数值列表。

```c
static const type_ z_ztest_param_arr_##name_[] = {__VA_ARGS__};                     \
static const struct ztest_param_values name_ = {                                     \
        .values       = z_ztest_param_arr_##name_,                                   \
        .count        = ARRAY_SIZE(z_ztest_param_arr_##name_),                       \
        .elem_size    = sizeof(type_),                                                \
        .name_cb      = NULL,                                                        \
        .value_at_cb  = NULL,                                                        \
        .setup_cb     = NULL,                                                        \
}
```

[`ZTEST_DEFINE_PARAM_VALUES_ARRAY`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gad40d44d71fa4f6c75a9ad44fffa30589) 从已有数组声明静态参数集合。

```c
#define ZTEST_DEFINE_PARAM_VALUES_ARRAY(name_, array_)
```

`name_` 为结果变量标识符，`array_` 为参数值数组，**必须在宏调用位置的作用域中可见**。

```c
static const struct ztest_param_values name_ = {                                     \
        .values      = (array_),                                                     \
        .count       = ARRAY_SIZE(array_),                                           \
        .elem_size   = sizeof((array_)[0]),                                          \
        .name_cb     = NULL,                                                         \
        .value_at_cb = NULL,                                                         \
        .setup_cb    = NULL,                                                         \
}
```

## 507.4\_将预期失败或跳过视为通过

[`ZTEST_EXPECT_FAIL`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaeaa5b96855dd45e015b9556212f8945a) 指定一个测试预期失败；若实际失败，就将其视为通过。参数 `_suite_name` 是套件名，`_test_name` 是测试名。

```c
#define ZTEST_EXPECT_FAIL(_suite_name, _test_name)
```

内部 `__ZTEST_EXPECT` 注册预期结果，[`ZTEST_EXPECTED_RESULT_FAIL`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d) 表示预期失败：

```c
__ZTEST_EXPECT(_suite_name, _test_name, ZTEST_EXPECTED_RESULT_FAIL)
```

官方示例使用 `zassert_true` 真值断言制造失败；`false` 为布尔假值。

```c
ZTEST_EXPECT_FAIL(my_suite, test_x);
ZTEST(my_suite, text_x) {
  zassert_true(false, NULL);
}
```

[`ZTEST_EXPECT_SKIP`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacb6f06920e522b9a9f6e7a98f0620f38) 指定预期跳过的测试，参数仍为套件名和测试名。

```c
#define ZTEST_EXPECT_SKIP(_suite_name, _test_name)
```

```c
__ZTEST_EXPECT(_suite_name, _test_name, ZTEST_EXPECTED_RESULT_SKIP)
```

官方示例用 `zassume_true` 假设检查触发跳过：

```c
ZTEST_EXPECT_SKIP(my_suite, test_x);
ZTEST(my_suite, text_x) {
  zassume_true(false, NULL);
}
```

> 译注：两个原示例注册的是 `test_x`，实际定义却写成 `text_x`，应在实际测试中统一名称。[`ZTEST_EXPECT_SKIP`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacb6f06920e522b9a9f6e7a98f0620f38) 的原说明把“失败后通过”复制到了跳过场景；宏展开明确注册 [`ZTEST_EXPECTED_RESULT_SKIP`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a)。这里按宏目的说明为预期跳过，并保留原始展开与示例。

## 507.5\_夹具、参数读取与参数实例化

[`ZTEST_F`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacd3ab522e0e5c8a270e86b0cb6bd81b2) 与 [`ZTEST()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac25858f76ea667d07de422a3b489cb15) 一样定义测试，但测试函数接收一个名为 `fixture`、类型为 `struct suite##_fixture *` 的夹具参数。`suite` 为所属套件名，`fn` 为测试函数名。

```c
#define ZTEST_F(suite, fn)
```

```c
Z_ZTEST_F(suite, fn, 0)
```

[`ZTEST_GET_PARAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac597d23f0c79eeff95d85e2a88c04836) 按指定类型取得当前参数值；`type` 是所需 C 类型。

```c
#define ZTEST_GET_PARAM(type)
```

```c
(*ZTEST_GET_PARAM_PTR(type))
```

[`ZTEST_GET_PARAM_PTR`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga4931b348affd96312e49317730da8921) 按指定类型取得当前参数的只读指针：

```c
#define ZTEST_GET_PARAM_PTR(type)
```

```c
((const type *)ztest_get_current_param())
```

[`ZTEST_INSTANTIATE_TEST_SUITE_P`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga98baeb865dcc55c1880fd2c6f8771ad3) 将一组参数值绑定到一个 [`ZTEST_P`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gab80e25231b291b2c2b32e6049a52d34c) 测试，在 [`ztest_param_inst`](P512_参数化测试注册结构.md) 链接段注册一条记录。套件执行时，对参数集合中的每个值调用一次测试函数，并在每次调用前设置参数上下文。在函数体内可用 [`ztest_get_current_param()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga9d7fcc3e316762a9a729f48e71819db7) 或 [`ZTEST_GET_PARAM()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac597d23f0c79eeff95d85e2a88c04836) 取值。

```c
#define ZTEST_INSTANTIATE_TEST_SUITE_P(inst_, suite_, fn_, param_values_name_)
```

`setup()` 返回的套件夹具作为 `ZTEST_P` 函数的 `data` 参数传入，**绝不会被参数值覆盖**。

| 参数 | 含义 |
| --- | --- |
| `inst_` | 此次实例化的唯一标识符 |
| `suite_` | 套件名称，必须与 [`ZTEST_SUITE`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaef8892743e2d47c983efcb61beeedeb3) 声明匹配 |
| `fn_` | 测试名称，必须由 `ZTEST_P` 声明 |
| `param_values_name_` | 参数集合变量名称；本参数说明列举了 [`ZTEST_DEFINE_PARAM_VALUES()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga37db3f58e35fdf40096ebad3f55e68ef) 和 [`ZTEST_DEFINE_PARAM_VALUES_ARRAY()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gad40d44d71fa4f6c75a9ad44fffa30589) |

```c
static const STRUCT_SECTION_ITERABLE(                                                \
        ztest_param_inst,                                                            \
        UTIL_CAT(UTIL_CAT(z_ztest_param_inst_, suite_),                              \
                 UTIL_CAT(_, UTIL_CAT(fn_, UTIL_CAT(_, inst_))))) = {               \
        .test_suite_name = STRINGIFY(suite_),                                        \
        .test_name       = STRINGIFY(fn_),                                           \
        .instance_name   = STRINGIFY(inst_),                                         \
        .values          = &(param_values_name_),                                    \
}
```

`ZTEST_P` 定义值参数化测试，原页对它只提供以下声明与展开；其 `suite` 和 `fn` 分别标识套件及测试函数。

```c
#define ZTEST_P(suite, fn)
```

```c
Z_TEST_P(suite, fn, 0)
```

## 507.6\_测试规则与指定套件运行

[`ZTEST_RULE`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2a0a5e3b6e8fa1c9a03e7600895d875f) 定义在**每个套件的每个单元测试**之前或之后执行的测试规则（Test Rule）。回调得到当前测试的指针及其数据，可以根据具体测试或数据执行操作，例如按测试名记录日志。

```c
#define ZTEST_RULE(name, before_each_fn, after_each_fn)
```

`name` 是规则名，必须在编译单元内唯一；`before_each_fn`、`after_each_fn` 是 [`ztest_rule_cb`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2090c493018a95112b89c5f83b5d8162) 类型的测试前/后回调，均可为 `NULL`。

规则的前置回调先于套件的前置回调执行，以便套件定制覆盖适用于全部套件的规则设置。**规则的后置回调不保证任何特定执行顺序。**

```c
static STRUCT_SECTION_ITERABLE(ztest_test_rule, z_ztest_test_rule_##name) = {              \
        .before_each = (before_each_fn),                                                   \
        .after_each = (after_each_fn),                                                     \
}
```

[`ztest_run_test_suite`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac2ac069e393ea7480e78e85ed93238be) 运行指定套件：

```c
#define ztest_run_test_suite(suite, shuffle, suite_iter, case_iter, param)
```

`suite` 为待运行套件，`shuffle` 控制打乱测试顺序，`suite_iter` 为套件重复次数，`case_iter` 为测试用例重复次数，`param` 为测试参数。

```c
z_ztest_run_test_suite(STRINGIFY(suite), shuffle, suite_iter, case_iter, param)
```

## 507.7\_套件注册、统计数量与用户态

`ZTEST_SUITE` 创建并注册套件，在特定链接段中创建 `struct ztest_suite_node`。注册后可把当前状态传给 [`ztest_run_test_suites()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaafb3cba3a9637839952b2db2486ab88c) 来执行，完整签名见本章后文。

```c
#define ZTEST_SUITE(SUITE_NAME, PREDICATE, setup_fn, before_fn, after_fn, teardown_fn)
```

| 参数 | 含义 |
| --- | --- |
| `SUITE_NAME` | 套件名称 |
| `PREDICATE` | 根据状态判断是否应运行测试的谓词（Predicate）函数 |
| `setup_fn` | 整个套件运行前调用的准备函数 |
| `before_fn` | 套件内每个单元测试之前调用的函数 |
| `after_fn` | 套件内每个单元测试之后调用的函数 |
| `teardown_fn` | 套件全部测试运行后调用的清理函数 |

```c
struct ztest_suite_stats UTIL_CAT(z_ztest_suite_node_stats_, SUITE_NAME);                  \
static const STRUCT_SECTION_ITERABLE(ztest_suite_node,                                     \
                                     UTIL_CAT(z_ztest_test_node_, SUITE_NAME)) = {         \
        .name = STRINGIFY(SUITE_NAME),                                                     \
        .setup = (setup_fn),                                                               \
        .before = (before_fn),                                                             \
        .after = (after_fn),                                                               \
        .teardown = (teardown_fn),                                                         \
        .predicate = PREDICATE,                                                            \
        .stats = &UTIL_CAT(z_ztest_suite_node_stats_, SUITE_NAME),             \
}
```

> 译注：原说明写作仅传一个 [`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90) 参数的调用形式；本页当前函数声明还要求 `shuffle`、`suite_iter`、`case_iter`，应使用后文完整签名。

以下三个宏给出已注册单元测试数、参数化测试实例化数和套件数。`*_list_start` 与 `*_list_end` 是对应注册列表的边界符号。

```c
#define ZTEST_TEST_COUNT (_ztest_unit_test_list_end - _ztest_unit_test_list_start)
#define ZTEST_PARAM_INST_COUNT (_ztest_param_inst_list_end - _ztest_param_inst_list_start)
#define ZTEST_SUITE_COUNT (_ztest_suite_node_list_end - _ztest_suite_node_list_start)
```

**用户空间（User Space）**支持由 Kconfig 配置项 `CONFIG_USERSPACE` 控制。下面三个宏令 ZTest 使用的已初始化数据段、未显式初始化数据段及数据段名称可供用户态访问，绑定的内存分区为 [`ztest_mem_partition`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga3adced2fdda96833e6b1ecbf3d61d446)。[`K_APP_DMEM`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga11bca9fb974837421cfaa27d0958bcc7)、[`K_APP_BMEM`](../memory_domain_reference/P006_应用内存分区接口.md#ga8fd691f9c9007ec80432c19f7ce84881)、[`K_APP_DMEM_SECTION`](../memory_domain_reference/P006_应用内存分区接口.md#ga81962bb530118ffa13fccdf99f973787) 是相应的分区/段辅助宏。

```c
#define ZTEST_DMEM K_APP_DMEM(ztest_mem_partition)
#define ZTEST_BMEM K_APP_BMEM(ztest_mem_partition)
#define ZTEST_SECTION K_APP_DMEM_SECTION(ztest_mem_partition)
```

[`ZTEST_USER`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga7121acc7ee00646cacefa773ff9631c8) 与普通 `ZTEST` 相同，但启用 `CONFIG_USERSPACE` 时在用户空间调用测试函数。`suite` 为套件名，`fn` 为测试函数名，展开中的 [`K_USER`](../thread_core_reference/P001_线程公共接口.md#gacb5340339892f22301e02697c6039ccc) 是用户线程标志。

```c
#define ZTEST_USER(suite, fn)
```

```c
Z_ZTEST(suite, fn, K_USER)
```

[`ZTEST_USER_F`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga12ccce144e577cac6ba763982ad14def) 定义带夹具的用户线程测试。如果未启用 `CONFIG_USERSPACE`，其功能与 [`ZTEST_F()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacd3ab522e0e5c8a270e86b0cb6bd81b2) 相同。函数接收名为 `fixture` 的单个参数，类型为 `struct suite##_fixture *`。

```c
#define ZTEST_USER_F(suite, fn)
```

参数 `suite` 为所属套件，`fn` 为调用的测试函数。

```c
Z_ZTEST_F(suite, fn, K_USER)
```

[`ZTEST_USER_P`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5514ada813e1aa6cae183f4a7c8af583) 与 `ZTEST_P` 相同，但以 [`K_USER`](../thread_core_reference/P001_线程公共接口.md#gacb5340339892f22301e02697c6039ccc) 标志创建测试线程，启用 `CONFIG_USERSPACE` 时在用户空间执行。被测代码是**系统调用（System Call）**，或必须从无特权上下文测试时，应使用这个宏。

```c
#define ZTEST_USER_P(suite, fn)
```

`suite` 为套件名，`fn` 为测试函数名，必须配合 [`ZTEST_INSTANTIATE_TEST_SUITE_P()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga98baeb865dcc55c1880fd2c6f8771ad3) 使用。

```c
Z_TEST_P(suite, fn, K_USER)
```

## 507.8\_回调类型

以下六个完整函数指针类型分别服务于规则和套件生命周期。

```c
typedef void (*ztest_rule_cb)(const struct ztest_unit_test *test, void *data);
typedef void (*ztest_suite_after_t)(void *fixture);
typedef void (*ztest_suite_before_t)(void *fixture);
typedef bool (*ztest_suite_predicate_t)(const void *global_state);
typedef void *(*ztest_suite_setup_t)(void);
typedef void (*ztest_suite_teardown_t)(void *fixture);
```

[`ztest_rule_cb`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2090c493018a95112b89c5f83b5d8162) 用于规则的前/后回调。`test` 指向当前单元测试，`data` 指向夹具数据，允许为 `NULL`。

[`ztest_suite_before_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac8a204832c267fed047e7707b65be74d) 在套件内每个测试之前执行，[`ztest_suite_after_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0f9eeb8ddae455c1e7cc7a388a7b013c) 在每个测试之后执行；二者的 `fixture` 都是套件 `setup()` 返回的夹具。[`ztest_suite_setup_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0063907dd70b9eb817ea472162693ee4) 在整个套件之前执行，返回贯穿套件使用的数据结构指针；[`ztest_suite_teardown_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga7769b894fdac5283ac949ce8fceea0dd) 在套件之后执行，参数为准备函数返回的数据。

[`ztest_suite_predicate_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gad5323aa82773dac33cf0930e9524420c) 是可选谓词。`global_state` 为当前测试应用状态，返回 `true` 表示运行套件，返回 `false` 表示跳过。**谓词为 `NULL` 时，测试只在第一次尝试时运行一次。**

## 507.9\_预期结果、执行阶段与当前结果

[`ztest_expected_result`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaf4dfaad1b5f1059e87f406979769aa26) 表示预期结果，供 [`ZTEST_EXPECT_FAIL`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaeaa5b96855dd45e015b9556212f8945a)、`ZTEST_EXPECT_SKIP` 使用：

```c
enum ztest_expected_result {
    ZTEST_EXPECTED_RESULT_FAIL = 0,
    ZTEST_EXPECTED_RESULT_SKIP
};
```

前者预期失败。后者原字段说明写作“预期测试通过”，与名称及注册宏不一致；译注：此成员用于预期跳过的记录，不将该说明当作预期普通通过的接口。

[`ztest_phase`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5dde8913cf45656bca8a48c825a95d59) 的每个成员表示测试可执行程序的一个执行阶段。内部 ZTest 代码执行时使用 [`TEST_PHASE_FRAMEWORK`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971)；其他成员对应用户测试代码阶段。

各枚举成员中，`TEST_PHASE_SETUP` 表示套件准备，`TEST_PHASE_BEFORE` 表示测试前，`TEST_PHASE_TEST` 表示测试体，`TEST_PHASE_AFTER` 表示测试后，`TEST_PHASE_TEARDOWN` 表示套件清理。

```c
enum ztest_phase {
    TEST_PHASE_SETUP,
    TEST_PHASE_BEFORE,
    TEST_PHASE_TEST,
    TEST_PHASE_AFTER,
    TEST_PHASE_TEARDOWN,
    TEST_PHASE_FRAMEWORK
};
```

[`ztest_result`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac2842295307e7286d256bb179be60b02) 表示当前测试结果。准备函数可能将结果设为 `ZTEST_RESULT_SUITE_*`，使失败或跳过适用于套件内每个测试。

各枚举成员依次为待定 `ZTEST_RESULT_PENDING`、通过 `ZTEST_RESULT_PASS`、失败 `ZTEST_RESULT_FAIL`、跳过 `ZTEST_RESULT_SKIP`、套件跳过 `ZTEST_RESULT_SUITE_SKIP` 及套件失败 `ZTEST_RESULT_SUITE_FAIL`。

```c
enum ztest_result {
    ZTEST_RESULT_PENDING,
    ZTEST_RESULT_PASS,
    ZTEST_RESULT_FAIL,
    ZTEST_RESULT_SKIP,
    ZTEST_RESULT_SUITE_SKIP,
    ZTEST_RESULT_SUITE_FAIL
};
```

## 507.10\_参数上下文查询

下面四个函数读取当前值参数化测试上下文。

```c
const void *ztest_get_current_param(void);
size_t ztest_get_current_param_index(void);
size_t ztest_get_current_param_size(void);
bool ztest_has_current_param(void);
```

[`ztest_get_current_param()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga9d7fcc3e316762a9a729f48e71819db7) 返回当前活动参数，非参数化测试返回 `NULL`。[`ztest_get_current_param_index()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0edd9f03977918a4fe4f4ed1e59ef3e1) 返回当前参数索引，非参数化测试返回 `0`。[`ztest_get_current_param_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5b6ba1f30dfeb11d48a176e8f3a31292) 返回当前参数元素的字节数，非参数化测试返回 `0`。[`ztest_has_current_param()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gabfd65eebc03c9064dcffdd47fa833961) 在当前运行的是值参数化实例时返回 `true`。

## 507.11\_运行与覆盖检查

[`ztest_run_all()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac6b1f8b820cd682094b7aaeebdaa106e) 是运行或列出已注册单元测试的默认入口；`ztest_run_test_suites()` 运行谓词返回 `true` 的已注册测试，并返回实际运行的测试数量。

```c
void ztest_run_all(const void *state, bool shuffle, int suite_iter, int case_iter);
int ztest_run_test_suites(const void *state, bool shuffle, int suite_iter, int case_iter);
```

两个函数的参数含义相同：[`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90) 为与测试可执行程序有关的当前机器状态，`shuffle` 控制打乱顺序，`suite_iter` 为套件重复次数，`case_iter` 为用例重复次数。

[`ztest_verify_all_test_suites_ran()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga349fda278dff713debfd2a3b94b8b1eb) 在存在已注册但从未执行的套件时使测试失败。

```c
void ztest_verify_all_test_suites_ran(void);
```

套件可能因为注册时提供的判断函数一直阻止执行而从未运行。需要确保所有套件至少执行一次时，可在 [`test_main()`](https://docs.zephyrproject.org/latest/doxygen/html/ztest_8h.html#a8a4533f287d99bb2d7c24c0e29c9a449) 末尾调用该函数。

> 译注：原文将上述判断函数写作 “pragma function”；同页套件注册使用的是谓词 `PREDICATE`，此处按其用途译为判断函数。

## 507.12\_通过、失败、跳过与单CPU辅助回调

以下函数控制当前测试结果：

```c
void ztest_test_fail(void);
void ztest_test_pass(void);
void ztest_test_skip(void);
void ztest_skip_failed_assumption(void);
```

[`ztest_test_fail()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacd6eb423f54dce8544f7c3b1618c0374) 使当前测试失败，失败断言等会调用它，通常无需手工调用。[`ztest_test_skip()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gada3b1fcfa71db1bf7787c03ff45256d5) 跳过当前测试。原页只给出 [`ztest_skip_failed_assumption()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga17537c79021fbc12e56b72ccec4b99c5) 声明，没有进一步行为说明。

[`ztest_test_pass()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga085d30a04102ebb8c3f2206020723ee0) 使当前测试通过。通常测试只需在没有断言失败时正常返回；若预期成功场景本身涉及**致命故障（Fatal Fault）**，可在 `k_sys_fatal_error_handler` 致命错误处理函数中调用它，在中止线程之前标记测试已通过。

下面两个辅助回调用于需要启动或停止 `1cpu` 机制的套件。这里 CPU 指**中央处理器（Central Processing Unit）**；具体机制由对应 `z_test_1cpu_*` 函数提供。

```c
void ztest_simple_1cpu_before(void *data);
void ztest_simple_1cpu_after(void *data);
```

二者均忽略代表套件数据的 `data` 参数；前者调用 `z_test_1cpu_start()`，后者调用 `z_test_1cpu_stop()`。

## 507.13\_后端、执行线程栈与内存分区

当前活动的 ZTest **后端（Backend）**实例为 `ztest_api`。默认执行器、命令行执行器（Shell Runner）或可移植操作系统接口（Portable Operating System Interface，POSIX）执行器中，恰有一个提供它的定义，其他后端在这里声明它，确保每个定义前都有可见声明。

```c
extern K_APP_DMEM(ztest_mem_partition) const struct ztest_arch_api ztest_api;
```

`ztest_thread_stack` 是测试执行线程使用的**栈（Stack）**，由当前活动后端定义。此处先声明，以满足 MISRA C:2012 Rule 8.4 的先行可见声明要求，同时让检查执行线程栈的测试（例如用户态内存保护测试）能够引用它。MISRA C 是 C 语言编码规范名称，此处沿用官方规则编号。

其中 Kconfig 配置项 `CONFIG_ZTEST_STACK_SIZE` 给出 ZTest 栈大小，`CONFIG_TEST_EXTRA_STACK_SIZE` 给出测试额外栈大小；声明使用两者之和。

```c
K_THREAD_STACK_DECLARE(ztest_thread_stack,
                       CONFIG_ZTEST_STACK_SIZE + CONFIG_TEST_EXTRA_STACK_SIZE);
```

[`K_THREAD_STACK_DECLARE`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaf08bc3a6bd253ca819ac93aa9f9d4f09) 为线程栈声明宏，两个 `CONFIG_*` 项分别提供 ZTest 栈大小与测试额外栈大小。内存分区变量声明为：

```c
extern struct k_mem_partition ztest_mem_partition;
```

[`k_mem_partition`](../memory_domain_reference/P005_内存分区结构.md) 是内存分区结构类型；原页没有进一步变量说明。

---

[上一章：ZTest模拟支持](P506_ZTest模拟支持.md) · [下一章：ZTest压力测试宏](P508_ZTest压力测试宏.md) · [返回大纲](大纲.md)
