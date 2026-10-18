---
id: learning.zephyr-docs.api-source-reference.page-816
title: state.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/state_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第816章\_state.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/state_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P071_电源状态头文件.md)。

## 816.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00030"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00042"></a>
<a id="l00053"></a>
<a id="l00065"></a>
<a id="l00077"></a>
<a id="l00089"></a>
<a id="l00102"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00187"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="foldopen00253"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="foldopen00327"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="foldopen00374"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="foldopen00385"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="foldopen00406"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="foldopen00423"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="adevicetree_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__subsys__pm__states_html_ga20e2f5ea9027a3653e5b9cc5aa1e21d5"></a>
<a id="agroup__subsys__pm__states_html_ga5263154fead1bae9d35166b176a14055"></a>
<a id="agroup__subsys__pm__states_html_ga682f75eb5324455ce95a5c7d4c2d6242"></a>
<a id="agroup__subsys__pm__states_html_ga7ae95c361448060420843c2ae6342f9c"></a>
<a id="agroup__subsys__pm__states_html_gaa8b05b5453f956f424f439ff12b4e3f4"></a>
<a id="agroup__subsys__pm__states_html_gac3b058822bd4f9e73c8ef053fd66bdba"></a>
<a id="agroup__subsys__pm__states_html_gga20e2f5ea9027a3653e5b9cc5aa1e21d5a18d180711616cd9ed59fbe27dd0dbf01"></a>
<a id="agroup__subsys__pm__states_html_gga20e2f5ea9027a3653e5b9cc5aa1e21d5a19a09872876d4732d0aebb82e52f2429"></a>
<a id="agroup__subsys__pm__states_html_gga20e2f5ea9027a3653e5b9cc5aa1e21d5a363669b6a6db4bee5b8196442e9f2a00"></a>
<a id="agroup__subsys__pm__states_html_gga20e2f5ea9027a3653e5b9cc5aa1e21d5a383b8ef562f50d7a3d18914d3c950743"></a>
<a id="agroup__subsys__pm__states_html_gga20e2f5ea9027a3653e5b9cc5aa1e21d5a73c76572bc04e999d22a3bded9c54b19"></a>
<a id="agroup__subsys__pm__states_html_gga20e2f5ea9027a3653e5b9cc5aa1e21d5a781f940d30738d746eb2523155950fc0"></a>
<a id="agroup__subsys__pm__states_html_gga20e2f5ea9027a3653e5b9cc5aa1e21d5a97c44ed1a8b6873243d6bbd76a382737"></a>
<a id="agroup__subsys__pm__states_html_gga20e2f5ea9027a3653e5b9cc5aa1e21d5acc7f38698db1ae08365115f8407c9695"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructpm__state__constraint_html"></a>
<a id="astructpm__state__constraint_html_a1007d7769f3529bb91db30fc503964ad"></a>
<a id="astructpm__state__constraint_html_aabbdf004f6cbf8a5464f03cb63bb518e"></a>
<a id="astructpm__state__constraints_html"></a>
<a id="astructpm__state__constraints_html_a1a4b1ecf767148ef1ebed535369291a0"></a>
<a id="astructpm__state__constraints_html_a248e920d4b1bcfe5834a9afd2ca48667"></a>
<a id="astructpm__state__info_html"></a>
<a id="astructpm__state__info_html_a422bc0c9aedc107dbfa57c3ac8eb2445"></a>
<a id="astructpm__state__info_html_a442654715d3872de1b7b0dcf08bffb8b"></a>
<a id="astructpm__state__info_html_a6fc8e0a78df78c7a28a0bc2a27292818"></a>
<a id="astructpm__state__info_html_ac0a5ee091648225ba25ea34c75163814"></a>
<a id="astructpm__state__info_html_aed57fc8a935951aa2687614b954c7225"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Intel corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_PM_STATE_H_
#define ZEPHYR_INCLUDE_PM_STATE_H_

#include <zephyr/sys/util.h>
#include <zephyr/devicetree.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif


enum pm_state {
        PM_STATE_ACTIVE,
        PM_STATE_RUNTIME_IDLE,
        PM_STATE_SUSPEND_TO_IDLE,
        PM_STATE_STANDBY,
        PM_STATE_SUSPEND_TO_RAM,
        PM_STATE_SUSPEND_TO_DISK,
        PM_STATE_SOFT_OFF,
        PM_STATE_COUNT,
};

struct pm_state_info {
        enum pm_state state;

        uint8_t substate_id;

        bool pm_device_disabled;

        uint32_t min_residency_us;

        uint32_t exit_latency_us;
};

struct pm_state_constraint {
        enum pm_state state;
        uint8_t substate_id;
};

struct pm_state_constraints {
        struct pm_state_constraint *list;
        size_t count;
};


#define Z_DT_PHANDLE_01(node_id, prop, idx) \
        COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(DT_PHANDLE_BY_IDX(node_id, prop, idx)), \
                    (1), (0))

#define Z_PM_STATE_INFO_FROM_DT_CPU(i, node_id)                                                   \
        COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(DT_PHANDLE_BY_IDX(node_id, cpu_power_states, i)),     \
                    (PM_STATE_INFO_DT_INIT(DT_PHANDLE_BY_IDX(node_id, cpu_power_states, i)),), ())

#define Z_PM_STATE_FROM_DT_CPU(i, node_id)                                                        \
        COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(DT_PHANDLE_BY_IDX(node_id, cpu_power_states, i)),     \
                    (PM_STATE_DT_INIT(DT_PHANDLE_BY_IDX(node_id, cpu_power_states, i)),), ())


#define PM_STATE_INFO_DT_INIT(node_id)                                         \
        {                                                                      \
                .state = PM_STATE_DT_INIT(node_id),                            \
                .substate_id = DT_PROP_OR(node_id, substate_id, 0),            \
                .min_residency_us = DT_PROP_OR(node_id, min_residency_us, 0),  \
                .exit_latency_us = DT_PROP_OR(node_id, exit_latency_us, 0),    \
                .pm_device_disabled = DT_PROP(node_id, zephyr_pm_device_disabled),    \
        }

#define PM_STATE_DT_INIT(node_id) \
        DT_ENUM_IDX(node_id, power_state_name)

#define DT_NUM_CPU_POWER_STATES(node_id)                                                           \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, cpu_power_states),                                   \
                    (DT_FOREACH_PROP_ELEM_SEP(node_id, cpu_power_states, Z_DT_PHANDLE_01, (+))),   \
                    (0))

#define PM_STATE_INFO_LIST_FROM_DT_CPU(node_id)                                \
        {                                                                      \
                LISTIFY(DT_PROP_LEN_OR(node_id, cpu_power_states, 0),          \
                        Z_PM_STATE_INFO_FROM_DT_CPU, (), node_id)              \
        }

#define PM_STATE_LIST_FROM_DT_CPU(node_id)                                     \
        {                                                                      \
                LISTIFY(DT_PROP_LEN_OR(node_id, cpu_power_states, 0),          \
                        Z_PM_STATE_FROM_DT_CPU, (), node_id)                   \
        }

#define PM_STATE_CONSTRAINT_INIT(node_id)                                     \
        {                                                                     \
                .state = PM_STATE_DT_INIT(node_id),                           \
                .substate_id = DT_PROP_OR(node_id, substate_id, 0),           \
        }

#define Z_PM_STATE_CONSTRAINT_REF(node_id, phandle, idx)                        \
        PM_STATE_CONSTRAINT_INIT(DT_PHANDLE_BY_IDX(node_id, phandle, idx))

#define Z_PM_STATE_CONSTRAINTS_LIST_NAME(node_id, phandles)                   \
        CONCAT(node_id, _, phandles, _constraints)

#define PM_STATE_CONSTRAINTS_LIST_DEFINE(node_id, prop)                                    \
        struct pm_state_constraint Z_PM_STATE_CONSTRAINTS_LIST_NAME(node_id, prop)[] =     \
        {                                                                                  \
                DT_FOREACH_PROP_ELEM_SEP(node_id, prop, Z_PM_STATE_CONSTRAINT_REF, (,))    \
        }

#define PM_STATE_CONSTRAINTS_GET(node_id, prop)                                            \
        {                                                                                  \
                .list = Z_PM_STATE_CONSTRAINTS_LIST_NAME(node_id, prop),                   \
                .count = DT_PROP_LEN(node_id, prop),                                       \
        }

#if defined(CONFIG_PM) || defined(__DOXYGEN__)
uint8_t pm_state_cpu_get_all(uint8_t cpu, const struct pm_state_info **states);

const struct pm_state_info *pm_state_get(uint8_t cpu, enum pm_state state, uint8_t substate_id);

const char *pm_state_to_str(enum pm_state state);


int pm_state_from_str(const char *name, enum pm_state *out);

bool pm_state_in_constraints(const struct pm_state_constraints *constraints,
                             const struct pm_state_constraint match);


#else  /* CONFIG_PM */

static inline uint8_t pm_state_cpu_get_all(uint8_t cpu, const struct pm_state_info **states)
{
        ARG_UNUSED(cpu);
        ARG_UNUSED(states);

        return 0;
}

static inline const struct pm_state_info *pm_state_get(uint8_t cpu,
                                                       enum pm_state state,
                                                       uint8_t substate_id)
{
        ARG_UNUSED(cpu);
        ARG_UNUSED(state);
        ARG_UNUSED(substate_id);

        return NULL;
}

static inline bool pm_state_in_constraints(const struct pm_state_constraints *constraints,
                                           const struct pm_state_constraint match)
{
        ARG_UNUSED(constraints);
        ARG_UNUSED(match);

        return false;
}
#endif /* CONFIG_PM */

#ifdef __cplusplus
}
#endif

#endif
```

## 816.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 488 行

条件编译配置（Configuration）标记：`CONFIG_PM`。

### 注释 3：原第 517 行

条件编译配置（Configuration）标记：`CONFIG_PM`。

## 816.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P071_电源状态头文件.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [pm_state](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)
- [PM_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a383b8ef562f50d7a3d18914d3c950743)
- [PM_STATE_RUNTIME_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a73c76572bc04e999d22a3bded9c54b19)
- [PM_STATE_SUSPEND_TO_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a781f940d30738d746eb2523155950fc0)
- [PM_STATE_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a19a09872876d4732d0aebb82e52f2429)
- [PM_STATE_SUSPEND_TO_RAM](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a363669b6a6db4bee5b8196442e9f2a00)
- [PM_STATE_SUSPEND_TO_DISK](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5acc7f38698db1ae08365115f8407c9695)
- [PM_STATE_SOFT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a18d180711616cd9ed59fbe27dd0dbf01)
- [PM_STATE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a97c44ed1a8b6873243d6bbd76a382737)
- [pm_state_info](../power/P047_电源状态信息结构.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#aed57fc8a935951aa2687614b954c7225)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [substate_id](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#a422bc0c9aedc107dbfa57c3ac8eb2445)
- [pm_device_disabled](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#ac0a5ee091648225ba25ea34c75163814)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [min_residency_us](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#a442654715d3872de1b7b0dcf08bffb8b)
- [exit_latency_us](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#a6fc8e0a78df78c7a28a0bc2a27292818)
- [pm_state_constraint](../power/P045_电源状态约束结构.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__constraint.html#aabbdf004f6cbf8a5464f03cb63bb518e)
- [substate_id](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__constraint.html#a1007d7769f3529bb91db30fc503964ad)
- [pm_state_constraints](../power/P046_电源状态约束集合.md)
- [list](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__constraints.html#a1a4b1ecf767148ef1ebed535369291a0)
- [count](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__constraints.html#a248e920d4b1bcfe5834a9afd2ca48667)
- [pm_state_cpu_get_all](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#ga682f75eb5324455ce95a5c7d4c2d6242)
- [pm_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#ga7ae95c361448060420843c2ae6342f9c)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [pm_state_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gac3b058822bd4f9e73c8ef053fd66bdba)
- [pm_state_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gaa8b05b5453f956f424f439ff12b4e3f4)
- [pm_state_in_constraints](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#ga5263154fead1bae9d35166b176a14055)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [pm_state_constraint::substate_id](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__constraint.html#a1007d7769f3529bb91db30fc503964ad)
- [pm_state_constraint::state](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__constraint.html#aabbdf004f6cbf8a5464f03cb63bb518e)
- [pm_state_constraints::list](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__constraints.html#a1a4b1ecf767148ef1ebed535369291a0)
- [pm_state_constraints::count](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__constraints.html#a248e920d4b1bcfe5834a9afd2ca48667)
- [pm_state_info::substate_id](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#a422bc0c9aedc107dbfa57c3ac8eb2445)
- [pm_state_info::min_residency_us](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#a442654715d3872de1b7b0dcf08bffb8b)
- [pm_state_info::exit_latency_us](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#a6fc8e0a78df78c7a28a0bc2a27292818)
- [pm_state_info::pm_device_disabled](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#ac0a5ee091648225ba25ea34c75163814)
- [pm_state_info::state](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#aed57fc8a935951aa2687614b954c7225)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P815_stat_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P817_statistic.h_源码浏览.md)
