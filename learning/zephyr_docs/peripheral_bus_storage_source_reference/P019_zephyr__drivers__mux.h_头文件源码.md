---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-19
title: zephyr__drivers__mux.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr__drivers__mux.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P019_zephyr__drivers__mux.h_头文件参考.md)。

## 19.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00185"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="foldopen00271"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="foldopen00293"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adevicetree_2mux_8h_html"></a>
<a id="adevicetree_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__mux__interface_html_ga0e3cbbb7ac8796c3651b56c41dd1cec5"></a>
<a id="agroup__mux__interface_html_ga188b04add235e080b95ea293e7cfd276"></a>
<a id="agroup__mux__interface_html_ga69b883de5e7c90f797d5a07063089bbc"></a>
<a id="agroup__mux__interface_html_gad1b56b4430fca99f03bdf2b0ad6725c5"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructmux__control__driver__api_html"></a>
<a id="astructmux__control__driver__api_html_a0594f85b8a90eb1f2aa77c3b09ef9a33"></a>
<a id="astructmux__control__driver__api_html_a7f6eabe1190c03f4c3f88e75ffb5def1"></a>
<a id="astructmux__control__driver__api_html_a869779d5815628bb6ca7b7b9dd0258cd"></a>
<a id="astructmux__control_html"></a>
<a id="astructmux__control_html_a39c222d2b469939eddf03b75abe7001b"></a>
<a id="astructmux__control_html_a3c4c949a57de565642d00fe0b6380ad7"></a>
<a id="astructmux__state_html"></a>
<a id="astructmux__state_html_a89ec6f427ae2b928694d953178cfc284"></a>
<a id="astructmux__state_html_af1b91ac4571fd44b8138ca6b226d3812"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MUX_H_
#define ZEPHYR_INCLUDE_DRIVERS_MUX_H_


#include <errno.h>
#include <stddef.h>

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/devicetree/mux.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

struct mux_control {
        const uint32_t *cells;
        size_t len;
};

struct mux_state {
        const struct mux_control *control;
        uint32_t state;
};


#define Z_MUX_CTRL_DEFINE_BY_IDX(node_id, idx)                                                  \
        static const uint32_t Z_MUX_CTRL_CELLS_NAME(node_id, idx)[] = {                         \
                COND_CODE_1(IS_EQ(Z_MUX_PHA_NUM_CELLS(node_id, mux_controls, idx), 0),          \
                            (0),                                                                \
                            (DT_FOREACH_PHA_CELL_BY_IDX_SEP(node_id, mux_controls, idx,         \
                                                            Z_MUX_CELL_VAL, (,))))              \
        };                                                                                      \
        static const struct mux_control Z_MUX_CTRL_OBJ_NAME(node_id, idx) = {                   \
                .cells = Z_MUX_CTRL_CELLS_NAME(node_id, idx),                                   \
                .len = Z_MUX_PHA_NUM_CELLS(node_id, mux_controls, idx),                         \
        }

#define Z_MUX_STATE_DEFINE_BY_IDX(node_id, idx)                                                 \
        static const uint32_t Z_MUX_STATE_CELLS_NAME(node_id, idx)[] = {                        \
                COND_CODE_1(IS_EQ(Z_MUX_PHA_NUM_CELLS(node_id, mux_states, idx), 1),            \
                            (0),                                                                \
                            (Z_MUX_STATE_ADDRESSING_CELLS(node_id, idx)))                       \
        };                                                                                      \
        static const struct mux_control Z_MUX_STATE_CTRL_NAME(node_id, idx) = {                 \
                .cells = Z_MUX_STATE_CELLS_NAME(node_id, idx),                                  \
                .len = Z_MUX_PHA_NUM_CELLS(node_id, mux_states, idx) - 1,                       \
        };                                                                                      \
        static const struct mux_state Z_MUX_STATE_OBJ_NAME(node_id, idx) = {                    \
                .control = &Z_MUX_STATE_CTRL_NAME(node_id, idx),                                \
                .state = Z_MUX_STATE_LAST_CELL(node_id, idx),                                   \
        }


#define MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id, idx) Z_MUX_CTRL_DEFINE_BY_IDX(node_id, idx)

#define MUX_CONTROL_DT_SPEC_DEFINE(node_id) MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id, 0)

#define MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME(node_id, name) \
        MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id,        \
                DT_PHA_ELEM_IDX_BY_NAME(node_id, mux_controls, name))

#define MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id, idx) Z_MUX_STATE_DEFINE_BY_IDX(node_id, idx)

#define MUX_STATE_DT_SPEC_DEFINE(node_id) MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id, 0)

#define MUX_STATE_DT_SPEC_DEFINE_BY_NAME(node_id, name) \
        MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id,        \
                DT_PHA_ELEM_IDX_BY_NAME(node_id, mux_states, name))


typedef int (*mux_control_set_fn)(const struct device *dev,
                                  const struct mux_control *control,
                                  uint32_t state);

typedef int (*mux_state_get_fn)(const struct device *dev,
                                const struct mux_control *control,
                                uint32_t *state);

typedef int (*mux_control_disconnect_fn)(const struct device *dev,
                                         const struct mux_control *control);


__subsystem struct mux_control_driver_api {
        mux_control_set_fn set;
        mux_state_get_fn get_state;
        mux_control_disconnect_fn disconnect;
};

__syscall int mux_control_set(const struct device *dev,
                              const struct mux_control *control,
                              uint32_t state);

static inline int z_impl_mux_control_set(const struct device *dev,
                                         const struct mux_control *control,
                                         uint32_t state)
{
        const struct mux_control_driver_api *api = DEVICE_API_GET(mux_control, dev);

        return api->set(dev, control, state);
}

__syscall int mux_state_apply(const struct device *dev,
                              const struct mux_state *mstate);

static inline int z_impl_mux_state_apply(const struct device *dev,
                                         const struct mux_state *mstate)
{
        const struct mux_control_driver_api *api = DEVICE_API_GET(mux_control, dev);

        return api->set(dev, mstate->control, mstate->state);
}

__syscall int mux_state_get(const struct device *dev,
                            const struct mux_control *control,
                            uint32_t *state);

static inline int z_impl_mux_state_get(const struct device *dev,
                                       const struct mux_control *control,
                                       uint32_t *state)
{
        const struct mux_control_driver_api *api = DEVICE_API_GET(mux_control, dev);

        if (api->get_state == NULL) {
                return -ENOSYS;
        }

        return api->get_state(dev, control, state);
}

__syscall int mux_control_disconnect(const struct device *dev,
                                     const struct mux_control *control);

static inline int z_impl_mux_control_disconnect(const struct device *dev,
                                                const struct mux_control *control)
{
        const struct mux_control_driver_api *api = DEVICE_API_GET(mux_control, dev);

        if (api->disconnect == NULL) {
                return -ENOSYS;
        }

        return api->disconnect(dev, control);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/mux.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_MUX_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 435 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MUX_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P019_zephyr__drivers__mux.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/devicetree/mux.h](../dt_connection_reference/P008_设备树多路复用器头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cells](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md#a39c222d2b469939eddf03b75abe7001b)
- [len](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md#a3c4c949a57de565642d00fe0b6380ad7)
- [mux_state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md)
- [control](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md#a89ec6f427ae2b928694d953178cfc284)
- [state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md#af1b91ac4571fd44b8138ca6b226d3812)
- [device](../device_reference/P002_设备对象结构.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [mux_control_driver_api](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md)
- [set](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md#a7f6eabe1190c03f4c3f88e75ffb5def1)
- [get_state](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md#a0594f85b8a90eb1f2aa77c3b09ef9a33)
- [disconnect](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md#a869779d5815628bb6ca7b7b9dd0258cd)
- [mux_control_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga69b883de5e7c90f797d5a07063089bbc)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [mux_state_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gad1b56b4430fca99f03bdf2b0ad6725c5)
- [mux_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga188b04add235e080b95ea293e7cfd276)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [mux_control_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#ga0e3cbbb7ac8796c3651b56c41dd1cec5)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [mux.h](../dt_connection_reference/P008_设备树多路复用器头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [mux_control_driver_api::get_state](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md#a0594f85b8a90eb1f2aa77c3b09ef9a33)
- [mux_control_driver_api::set](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md#a7f6eabe1190c03f4c3f88e75ffb5def1)
- [mux_control_driver_api::disconnect](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md#a869779d5815628bb6ca7b7b9dd0258cd)
- [mux_control::cells](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md#a39c222d2b469939eddf03b75abe7001b)
- [mux_control::len](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md#a3c4c949a57de565642d00fe0b6380ad7)
- [mux_state::control](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md#a89ec6f427ae2b928694d953178cfc284)
- [mux_state::state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md#af1b91ac4571fd44b8138ca6b226d3812)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P018_zephyr__drivers__mspi__mspi_dw.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__mgmt__osdp.h_头文件源码.md)
