---
id: learning.zephyr-docs.api-file-audio-test-reference.page-13
title: ____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest_test.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_ztest\_\_include\_\_zephyr\_\_ztest\_test.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr测试框架（Testing Framework）的_test。

<a id="details"></a>

```c
#include <zephyr/app_memory/app_memdomain.h>
#include <zephyr/init.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/util.h>
#include <stdbool.h>
#include <zephyr/syscalls/ztest_test.h>
```

查看此文件的源码。

Zephyr测试框架（Testing Framework）的_test。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_ztest_5Fexpected_5Fresult_5Fentry"></a>

```c
struct ztest_expected_result_entry
```

相关声明：[ztest_expected_result_entry](../hardware/P509_测试预期结果记录.md)。

单个预期结果条目（Expectation Entry），允许测试失败或跳过后仍视为通过。

<a id="r_ztest_5Funit_5Ftest"></a>

```c
struct ztest_unit_test
```

相关声明：[ztest_unit_test](../hardware/P510_单元测试记录结构.md)。

<a id="r_ztest_5Fparam_5Fvalues"></a>

```c
struct ztest_param_values
```

相关声明：[ztest_param_values](../hardware/P511_测试参数集合结构.md)。

值参数化测试（Value-Parameterized Tests）的参数值集合。

<a id="r_ztest_5Fparam_5Finst"></a>

```c
struct ztest_param_inst
```

相关声明：[ztest_param_inst](../hardware/P512_参数化测试注册结构.md)。

将测试映射到参数值集合（Parameter Value Set）的注册条目。

<a id="r_ztest_5Fsuite_5Fstats"></a>

```c
struct ztest_suite_stats
```

相关声明：[ztest_suite_stats](../hardware/P513_测试套件统计结构.md)。

ztest测试套件（Suite）的统计信息。

<a id="r_ztest_5Funit_5Ftest_5Fstats"></a>

```c
struct ztest_unit_test_stats
```

相关声明：[ztest_unit_test_stats](../hardware/P514_单元测试统计结构.md)。

<a id="r_ztest_5Fsuite_5Fnode"></a>

```c
struct ztest_suite_node
```

相关声明：[ztest_suite_node](../hardware/P515_测试套件节点结构.md)。

测试套件（Test Suite）的单个节点。

<a id="r_ztest_5Farch_5Fapi"></a>

```c
struct ztest_arch_api
```

相关声明：[ztest_arch_api](../hardware/P516_测试架构后端接口.md)。

架构专用API（Architecture Specific APIs）的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_gaeaa5b96855dd45e015b9556212f8945a"></a>

```c
#define ZTEST_EXPECT_FAIL(_suite_name, _test_name)
```

相关声明：[ZTEST_EXPECT_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaeaa5b96855dd45e015b9556212f8945a)。

预期测试失败（Expect Failure）；测试失败时将其标记为通过。

<a id="r_gacb6f06920e522b9a9f6e7a98f0620f38"></a>

```c
#define ZTEST_EXPECT_SKIP(_suite_name, _test_name)
```

相关声明：[ZTEST_EXPECT_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacb6f06920e522b9a9f6e7a98f0620f38)。

预期测试跳过（Expect Skip）；原文括注为“测试失败时将其标记为通过”。

<a id="r_ga8777ca60bd21cc128f64833bd7921b9c"></a>

```c
#define ZTEST_TEST_COUNT (_ztest_unit_test_list_end - _ztest_unit_test_list_start)
```

相关声明：[ZTEST_TEST_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga8777ca60bd21cc128f64833bd7921b9c)。

已注册单元测试数量（Number of Registered Unit Tests）。

<a id="r_ga9e8d10190290b85d3d0839144b63ef79"></a>

```c
#define ZTEST_PARAM_INST_COUNT (_ztest_param_inst_list_end - _ztest_param_inst_list_start)
```

相关声明：[ZTEST_PARAM_INST_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga9e8d10190290b85d3d0839144b63ef79)。

已注册值参数化测试实例数量（Number of Value-parameterized Test Instantiations）。

<a id="r_ga678b4ae96879c029e6e567a326bbf027"></a>

```c
#define ZTEST_SUITE_COUNT (_ztest_suite_node_list_end - _ztest_suite_node_list_start)
```

相关声明：[ZTEST_SUITE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga678b4ae96879c029e6e567a326bbf027)。

已注册测试套件数量（Number of Registered Test Suites）。

<a id="r_gaef8892743e2d47c983efcb61beeedeb3"></a>

```c
#define ZTEST_SUITE(SUITE_NAME, PREDICATE, setup_fn, before_fn, after_fn, teardown_fn)
```

相关声明：[ZTEST_SUITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaef8892743e2d47c983efcb61beeedeb3)。

创建并注册 ztest 测试套件（Suite）。

<a id="r_ga2c7d0aa85e7f320d582395c5ded90133"></a>

```c
#define ZTEST_DMEM K_APP_DMEM(ztest_mem_partition)
```

相关声明：[ZTEST_DMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2c7d0aa85e7f320d582395c5ded90133)、[K_APP_DMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga11bca9fb974837421cfaa27d0958bcc7)、[ztest_mem_partition](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga3adced2fdda96833e6b1ecbf3d61d446)。

使 Ztest 使用的数据段（Data Section）可从用户空间访问。

<a id="r_gac3de5965061b1164a8033712c9094e23"></a>

```c
#define ZTEST_BMEM K_APP_BMEM(ztest_mem_partition)
```

相关声明：[ZTEST_BMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac3de5965061b1164a8033712c9094e23)、[K_APP_BMEM](../memory_domain_reference/P006_应用内存分区接口.md#ga8fd691f9c9007ec80432c19f7ce84881)、[ztest_mem_partition](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga3adced2fdda96833e6b1ecbf3d61d446)。

使 Ztest 使用的 BSS 段（BSS Section）可从用户空间访问。

<a id="r_ga44777f5011728bbff63fe3639c1b4aa8"></a>

```c
#define ZTEST_SECTION K_APP_DMEM_SECTION(ztest_mem_partition)
```

相关声明：[ZTEST_SECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga44777f5011728bbff63fe3639c1b4aa8)、[K_APP_DMEM_SECTION](../memory_domain_reference/P006_应用内存分区接口.md#ga81962bb530118ffa13fccdf99f973787)、[ztest_mem_partition](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga3adced2fdda96833e6b1ecbf3d61d446)。

Ztest 数据段（Data Section），用于从用户空间访问数据。

<a id="r_ga4931b348affd96312e49317730da8921"></a>

```c
#define ZTEST_GET_PARAM_PTR(type)
```

相关声明：[ZTEST_GET_PARAM_PTR](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga4931b348affd96312e49317730da8921)。

以带类型的指针（Typed Pointer）获取当前参数。

<a id="r_gac597d23f0c79eeff95d85e2a88c04836"></a>

```c
#define ZTEST_GET_PARAM(type)
```

相关声明：[ZTEST_GET_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac597d23f0c79eeff95d85e2a88c04836)。

以带类型的值（Typed Value）获取当前参数。

<a id="r_ga37db3f58e35fdf40096ebad3f55e68ef"></a>

```c
#define ZTEST_DEFINE_PARAM_VALUES(name_, type_, ...)
```

相关声明：[ZTEST_DEFINE_PARAM_VALUES](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga37db3f58e35fdf40096ebad3f55e68ef)。

声明供 ZTEST_INSTANTIATE_TEST_SUITE_P() 使用的静态值集合（Static Value Set）。

<a id="r_gad40d44d71fa4f6c75a9ad44fffa30589"></a>

```c
#define ZTEST_DEFINE_PARAM_VALUES_ARRAY(name_, array_)
```

相关声明：[ZTEST_DEFINE_PARAM_VALUES_ARRAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gad40d44d71fa4f6c75a9ad44fffa30589)。

通过现有数组声明静态值集合（Static Value Set）。

<a id="r_gae5100e9440a1bea86a7840c24300efa0"></a>

```c
#define ZTEST_DEFINE_PARAM_RANGE(name_, type_, begin_, end_, step_)
```

相关声明：[ZTEST_DEFINE_PARAM_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gae5100e9440a1bea86a7840c24300efa0)。

声明供 ZTEST_INSTANTIATE_TEST_SUITE_P() 使用的数值范围（Numeric Range）。

<a id="r_gadd987aba574bae91f6c627cb1998e82d"></a>

```c
#define ZTEST_DEFINE_PARAM_GENERATOR(name_, type_, count_, gen_cb_)
```

相关声明：[ZTEST_DEFINE_PARAM_GENERATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gadd987aba574bae91f6c627cb1998e82d)。

声明在运行时生成的参数集合（Runtime-generated Parameter Set）。

<a id="r_ga86db43dc0e56f416e86ace064f3d40d2"></a>

```c
#define ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP(name_, type_, count_, setup_cb_, gen_cb_)
```

相关声明：[ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga86db43dc0e56f416e86ace064f3d40d2)。

声明带一次性准备步骤（One-time Setup）的运行时生成参数集合（Runtime-generated Parameter Set）。

<a id="r_ga98baeb865dcc55c1880fd2c6f8771ad3"></a>

```c
#define ZTEST_INSTANTIATE_TEST_SUITE_P(inst_, suite_, fn_, param_values_name_)
```

相关声明：[ZTEST_INSTANTIATE_TEST_SUITE_P](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga98baeb865dcc55c1880fd2c6f8771ad3)。

使用一组参数值实例化 ZTEST_P 测试。

<a id="r_gab80e25231b291b2c2b32e6049a52d34c"></a>

```c
#define ZTEST_P(suite, fn)
```

相关声明：[ZTEST_P](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gab80e25231b291b2c2b32e6049a52d34c)。

<a id="r_ga5514ada813e1aa6cae183f4a7c8af583"></a>

```c
#define ZTEST_USER_P(suite, fn)
```

相关声明：[ZTEST_USER_P](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5514ada813e1aa6cae183f4a7c8af583)。

定义以用户线程（User Thread）运行的值参数化测试函数（Value-parameterized Test Function）。

<a id="r_gac25858f76ea667d07de422a3b489cb15"></a>

```c
#define ZTEST(suite, fn)
```

相关声明：[ZTEST](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac25858f76ea667d07de422a3b489cb15)。

创建并注册新的单元测试（Unit Test）。

<a id="r_ga7121acc7ee00646cacefa773ff9631c8"></a>

```c
#define ZTEST_USER(suite, fn)
```

相关声明：[ZTEST_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga7121acc7ee00646cacefa773ff9631c8)。

定义应当以用户线程（User Thread）运行的测试函数。

<a id="r_gacd3ab522e0e5c8a270e86b0cb6bd81b2"></a>

```c
#define ZTEST_F(suite, fn)
```

相关声明：[ZTEST_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacd3ab522e0e5c8a270e86b0cb6bd81b2)。

定义测试函数（Test Function）。

<a id="r_ga12ccce144e577cac6ba763982ad14def"></a>

```c
#define ZTEST_USER_F(suite, fn)
```

相关声明：[ZTEST_USER_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga12ccce144e577cac6ba763982ad14def)。

定义应当以用户线程（User Thread）运行的测试函数。

<a id="r_ga2a0a5e3b6e8fa1c9a03e7600895d875f"></a>

```c
#define ZTEST_RULE(name, before_each_fn, after_each_fn)
```

相关声明：[ZTEST_RULE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2a0a5e3b6e8fa1c9a03e7600895d875f)。

定义在每个单元测试之前／之后运行的测试规则（Test Rule）。

<a id="r_gac2ac069e393ea7480e78e85ed93238be"></a>

```c
#define ztest_run_test_suite(suite, shuffle, suite_iter, case_iter, param)
```

相关声明：[ztest_run_test_suite](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac2ac069e393ea7480e78e85ed93238be)。

运行指定测试套件（Test Suite）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 13.3\_类型定义（Typedefs）

<a id="r_ga0063907dd70b9eb817ea472162693ee4"></a>

```c
typedef void *(* ztest_suite_setup_t) (void)
```

相关声明：[ztest_suite_setup_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0063907dd70b9eb817ea472162693ee4)。

运行此套件之前执行的准备函数（Setup Function）。

<a id="r_gac8a204832c267fed047e7707b65be74d"></a>

```c
typedef void(* ztest_suite_before_t) (void *fixture)
```

相关声明：[ztest_suite_before_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac8a204832c267fed047e7707b65be74d)。

此套件中每项测试之前运行的函数。

<a id="r_ga0f9eeb8ddae455c1e7cc7a388a7b013c"></a>

```c
typedef void(* ztest_suite_after_t) (void *fixture)
```

相关声明：[ztest_suite_after_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0f9eeb8ddae455c1e7cc7a388a7b013c)。

此套件中每项测试之后运行的函数。

<a id="r_ga7769b894fdac5283ac949ce8fceea0dd"></a>

```c
typedef void(* ztest_suite_teardown_t) (void *fixture)
```

相关声明：[ztest_suite_teardown_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga7769b894fdac5283ac949ce8fceea0dd)。

运行此套件之后执行的清理函数（Teardown Function）。

<a id="r_gad5323aa82773dac33cf0930e9524420c"></a>

```c
typedef bool(* ztest_suite_predicate_t) (const void *global_state)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ztest_suite_predicate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gad5323aa82773dac33cf0930e9524420c)。

可选的谓词函数（Predicate Function），用于决定是否运行测试。

<a id="r_ga2090c493018a95112b89c5f83b5d8162"></a>

```c
typedef void(* ztest_rule_cb) (const struct ztest_unit_test *test, void *data)
```

相关声明：[ztest_rule_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2090c493018a95112b89c5f83b5d8162)、[ztest_unit_test](../hardware/P510_单元测试记录结构.md)。

测试规则回调函数签名（Test Rule Callback Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.4\_枚举（Enumerations）

<a id="r_gaf4dfaad1b5f1059e87f406979769aa26"></a>

```c
enum ztest_expected_result { ZTEST_EXPECTED_RESULT_FAIL = 0 , ZTEST_EXPECTED_RESULT_SKIP }
```

相关声明：[ztest_expected_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaf4dfaad1b5f1059e87f406979769aa26)、[ZTEST_EXPECTED_RESULT_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d)、[ZTEST_EXPECTED_RESULT_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a)。

测试的预期结果（Expected Result）。

<a id="r_gac2842295307e7286d256bb179be60b02"></a>

```c
enum ztest_result { ZTEST_RESULT_PENDING , ZTEST_RESULT_PASS , ZTEST_RESULT_FAIL , ZTEST_RESULT_SKIP , ZTEST_RESULT_SUITE_SKIP , ZTEST_RESULT_SUITE_FAIL }
```

相关声明：[ztest_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac2842295307e7286d256bb179be60b02)、[ZTEST_RESULT_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc)、[ZTEST_RESULT_PASS](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e)、[ZTEST_RESULT_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888)、[ZTEST_RESULT_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4)、[ZTEST_RESULT_SUITE_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e)、[ZTEST_RESULT_SUITE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55)。

当前正在运行的测试的结果（Test Result）。

<a id="r_ga5dde8913cf45656bca8a48c825a95d59"></a>

```c
enum ztest_phase { TEST_PHASE_SETUP , TEST_PHASE_BEFORE , TEST_PHASE_TEST , TEST_PHASE_AFTER , TEST_PHASE_TEARDOWN , TEST_PHASE_FRAMEWORK }
```

相关声明：[ztest_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5dde8913cf45656bca8a48c825a95d59)、[TEST_PHASE_SETUP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf)、[TEST_PHASE_BEFORE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765)、[TEST_PHASE_TEST](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1)、[TEST_PHASE_AFTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663)、[TEST_PHASE_TEARDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901)、[TEST_PHASE_FRAMEWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971)。

每个枚举成员代表测试二进制程序的一个不同执行阶段（Execution Phase）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.5\_函数（Functions）

<a id="r_gac6b1f8b820cd682094b7aaeebdaa106e"></a>

```c
void ztest_run_all (const void *state, bool shuffle, int suite_iter, int case_iter)
```

相关声明：[ztest_run_all](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac6b1f8b820cd682094b7aaeebdaa106e)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

运行或列出已注册单元测试的默认入口点（Default Entry Point）。

<a id="r_gaafb3cba3a9637839952b2db2486ab88c"></a>

```c
int ztest_run_test_suites (const void *state, bool shuffle, int suite_iter, int case_iter)
```

相关声明：[ztest_run_test_suites](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaafb3cba3a9637839952b2db2486ab88c)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

运行已注册且谓词函数（Predicate Function）返回 true 的单元测试。

<a id="r_ga349fda278dff713debfd2a3b94b8b1eb"></a>

```c
void ztest_verify_all_test_suites_ran (void)
```

相关声明：[ztest_verify_all_test_suites_ran](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga349fda278dff713debfd2a3b94b8b1eb)。

任何已注册测试没有运行时，使测试失败。

<a id="r_gacd6eb423f54dce8544f7c3b1618c0374"></a>

```c
void ztest_test_fail (void)
```

相关声明：[ztest_test_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacd6eb423f54dce8544f7c3b1618c0374)。

使当前运行的测试失败（Fail）。

<a id="r_ga085d30a04102ebb8c3f2206020723ee0"></a>

```c
void ztest_test_pass (void)
```

相关声明：[ztest_test_pass](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga085d30a04102ebb8c3f2206020723ee0)。

使当前运行的测试通过（Pass）。

<a id="r_gada3b1fcfa71db1bf7787c03ff45256d5"></a>

```c
void ztest_test_skip (void)
```

相关声明：[ztest_test_skip](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gada3b1fcfa71db1bf7787c03ff45256d5)。

跳过当前测试（Skip）。

<a id="r_ga17537c79021fbc12e56b72ccec4b99c5"></a>

```c
void ztest_skip_failed_assumption (void)
```

相关声明：[ztest_skip_failed_assumption](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga17537c79021fbc12e56b72ccec4b99c5)。

<a id="r_ga9d7fcc3e316762a9a729f48e71819db7"></a>

```c
const void * ztest_get_current_param (void)
```

相关声明：[ztest_get_current_param](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga9d7fcc3e316762a9a729f48e71819db7)。

返回当前活动的值参数化测试参数（Value-parameterized Test Argument）。

<a id="r_ga0edd9f03977918a4fe4f4ed1e59ef3e1"></a>

```c
size_t ztest_get_current_param_index (void)
```

相关声明：[ztest_get_current_param_index](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0edd9f03977918a4fe4f4ed1e59ef3e1)。

返回当前活动的值参数化测试参数索引（Argument Index）。

<a id="r_ga5b6ba1f30dfeb11d48a176e8f3a31292"></a>

```c
size_t ztest_get_current_param_size (void)
```

相关声明：[ztest_get_current_param_size](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5b6ba1f30dfeb11d48a176e8f3a31292)。

返回当前参数元素大小（Parameter Element Size），单位为字节。

<a id="r_gabfd65eebc03c9064dcffdd47fa833961"></a>

```c
bool ztest_has_current_param (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ztest_has_current_param](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gabfd65eebc03c9064dcffdd47fa833961)。

当前正在运行值参数化测试实例（Value-parameterized Test Instance）时返回 true。

<a id="r_gac7ddc33b5a0d11e2ffa0a564019c5e3d"></a>

```c
void ztest_simple_1cpu_before (void *data)
```

相关声明：[ztest_simple_1cpu_before](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac7ddc33b5a0d11e2ffa0a564019c5e3d)。

用于仅需启动 1cpu 的测试套件的 before 函数。

<a id="r_gaa53486873430dd8fa978745d8a1d0686"></a>

```c
void ztest_simple_1cpu_after (void *data)
```

相关声明：[ztest_simple_1cpu_after](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaa53486873430dd8fa978745d8a1d0686)。

用于仅需停止 1cpu 的测试套件的 after 函数。

<a id="r_ga11bca9fb974837421cfaa27d0958bcc7"></a>

```c
K_APP_DMEM (ztest_mem_partition) const struct ztest_arch_api ztest_api
```

相关声明：[K_APP_DMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga11bca9fb974837421cfaa27d0958bcc7)、[ztest_mem_partition](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga3adced2fdda96833e6b1ecbf3d61d446)、[ztest_arch_api](../hardware/P516_测试架构后端接口.md)。

当前活动的 ztest 后端实例（Backend Instance）。

<a id="r_gaf08bc3a6bd253ca819ac93aa9f9d4f09"></a>

```c
K_THREAD_STACK_DECLARE (ztest_thread_stack, CONFIG_ZTEST_STACK_SIZE+CONFIG_TEST_EXTRA_STACK_SIZE)
```

相关声明：[K_THREAD_STACK_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaf08bc3a6bd253ca819ac93aa9f9d4f09)。

ztest 运行器线程（Runner Thread）使用的栈（Stack）。

<a id="r_a846fcbfbda9794cba2dcf1c34bd9be1b"></a>

```c
void sys_clock_tick_set (uint64_t tick)
```

相关声明：[sys_clock_tick_set](#a846fcbfbda9794cba2dcf1c34bd9be1b)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 13.6\_变量（Variables）

<a id="r_ga3adced2fdda96833e6b1ecbf3d61d446"></a>

```c
struct k_mem_partition ztest_mem_partition
```

相关声明：[k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)、[ztest_mem_partition](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga3adced2fdda96833e6b1ecbf3d61d446)。

## 13.7\_详细说明（Detailed Documentation）

<a id="a846fcbfbda9794cba2dcf1c34bd9be1b"></a>

### `sys_clock_tick_set()`

```c
void sys_clock_tick_set ( uint64_t tick)
```


## 13.8\_原页交叉引用（Cross References）

- [zephyr/app_memory/app_memdomain.h](../memory_domain_reference/P010_应用内存域头文件源码.md)
- [zephyr/init.h](../device_reference/P010_系统初始化头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P058_ztest_test.h_源码浏览.md)
- [ztest_expected_result_entry](../hardware/P509_测试预期结果记录.md)
- [ztest_unit_test](../hardware/P510_单元测试记录结构.md)
- [ztest_param_values](../hardware/P511_测试参数集合结构.md)
- [ztest_param_inst](../hardware/P512_参数化测试注册结构.md)
- [ztest_suite_stats](../hardware/P513_测试套件统计结构.md)
- [ztest_unit_test_stats](../hardware/P514_单元测试统计结构.md)
- [ztest_suite_node](../hardware/P515_测试套件节点结构.md)
- [ztest_arch_api](../hardware/P516_测试架构后端接口.md)
- [ZTEST_EXPECT_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaeaa5b96855dd45e015b9556212f8945a)
- [ZTEST_EXPECT_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacb6f06920e522b9a9f6e7a98f0620f38)
- [ZTEST_TEST_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga8777ca60bd21cc128f64833bd7921b9c)
- [ZTEST_PARAM_INST_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga9e8d10190290b85d3d0839144b63ef79)
- [ZTEST_SUITE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga678b4ae96879c029e6e567a326bbf027)
- [ZTEST_SUITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaef8892743e2d47c983efcb61beeedeb3)
- [ZTEST_DMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2c7d0aa85e7f320d582395c5ded90133)
- [K_APP_DMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga11bca9fb974837421cfaa27d0958bcc7)
- [ztest_mem_partition](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga3adced2fdda96833e6b1ecbf3d61d446)
- [ZTEST_BMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac3de5965061b1164a8033712c9094e23)
- [K_APP_BMEM](../memory_domain_reference/P006_应用内存分区接口.md#ga8fd691f9c9007ec80432c19f7ce84881)
- [ZTEST_SECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga44777f5011728bbff63fe3639c1b4aa8)
- [K_APP_DMEM_SECTION](../memory_domain_reference/P006_应用内存分区接口.md#ga81962bb530118ffa13fccdf99f973787)
- [ZTEST_GET_PARAM_PTR](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga4931b348affd96312e49317730da8921)
- [ZTEST_GET_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac597d23f0c79eeff95d85e2a88c04836)
- [ZTEST_DEFINE_PARAM_VALUES](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga37db3f58e35fdf40096ebad3f55e68ef)
- [ZTEST_INSTANTIATE_TEST_SUITE_P()](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga98baeb865dcc55c1880fd2c6f8771ad3)
- [ZTEST_DEFINE_PARAM_VALUES_ARRAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gad40d44d71fa4f6c75a9ad44fffa30589)
- [ZTEST_DEFINE_PARAM_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gae5100e9440a1bea86a7840c24300efa0)
- [ZTEST_DEFINE_PARAM_GENERATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gadd987aba574bae91f6c627cb1998e82d)
- [ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga86db43dc0e56f416e86ace064f3d40d2)
- [ZTEST_P](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gab80e25231b291b2c2b32e6049a52d34c)
- [ZTEST_USER_P](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5514ada813e1aa6cae183f4a7c8af583)
- [ZTEST](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac25858f76ea667d07de422a3b489cb15)
- [ZTEST_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga7121acc7ee00646cacefa773ff9631c8)
- [ZTEST_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacd3ab522e0e5c8a270e86b0cb6bd81b2)
- [ZTEST_USER_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga12ccce144e577cac6ba763982ad14def)
- [ZTEST_RULE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2a0a5e3b6e8fa1c9a03e7600895d875f)
- [ztest_run_test_suite](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac2ac069e393ea7480e78e85ed93238be)
- [ztest_suite_setup_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0063907dd70b9eb817ea472162693ee4)
- [ztest_suite_before_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac8a204832c267fed047e7707b65be74d)
- [ztest_suite_after_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0f9eeb8ddae455c1e7cc7a388a7b013c)
- [ztest_suite_teardown_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga7769b894fdac5283ac949ce8fceea0dd)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ztest_suite_predicate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gad5323aa82773dac33cf0930e9524420c)
- [ztest_rule_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2090c493018a95112b89c5f83b5d8162)
- [ztest_expected_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaf4dfaad1b5f1059e87f406979769aa26)
- [ZTEST_EXPECTED_RESULT_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d)
- [ZTEST_EXPECTED_RESULT_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a)
- [ztest_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac2842295307e7286d256bb179be60b02)
- [ZTEST_RESULT_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc)
- [ZTEST_RESULT_PASS](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e)
- [ZTEST_RESULT_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888)
- [ZTEST_RESULT_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4)
- [ZTEST_RESULT_SUITE_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e)
- [ZTEST_RESULT_SUITE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55)
- [ztest_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5dde8913cf45656bca8a48c825a95d59)
- [TEST_PHASE_SETUP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf)
- [TEST_PHASE_BEFORE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765)
- [TEST_PHASE_TEST](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1)
- [TEST_PHASE_AFTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663)
- [TEST_PHASE_TEARDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901)
- [TEST_PHASE_FRAMEWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971)
- [ztest_run_all](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac6b1f8b820cd682094b7aaeebdaa106e)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [ztest_run_test_suites](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaafb3cba3a9637839952b2db2486ab88c)
- [ztest_verify_all_test_suites_ran](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga349fda278dff713debfd2a3b94b8b1eb)
- [ztest_test_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacd6eb423f54dce8544f7c3b1618c0374)
- [ztest_test_pass](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga085d30a04102ebb8c3f2206020723ee0)
- [ztest_test_skip](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gada3b1fcfa71db1bf7787c03ff45256d5)
- [ztest_skip_failed_assumption](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga17537c79021fbc12e56b72ccec4b99c5)
- [ztest_get_current_param](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga9d7fcc3e316762a9a729f48e71819db7)
- [ztest_get_current_param_index](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0edd9f03977918a4fe4f4ed1e59ef3e1)
- [ztest_get_current_param_size](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5b6ba1f30dfeb11d48a176e8f3a31292)
- [ztest_has_current_param](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gabfd65eebc03c9064dcffdd47fa833961)
- [ztest_simple_1cpu_before](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac7ddc33b5a0d11e2ffa0a564019c5e3d)
- [ztest_simple_1cpu_after](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaa53486873430dd8fa978745d8a1d0686)
- [K_THREAD_STACK_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaf08bc3a6bd253ca819ac93aa9f9d4f09)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_zephyr__dt-bindings__clock__syna_sr100_clock.h_文件参考.md) · [返回大纲](大纲.md)
