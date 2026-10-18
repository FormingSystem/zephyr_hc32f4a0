---
id: learning.zephyr-docs.api-source-runtime-reference.page-13
title: emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)。

## 13.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="foldopen00148"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="foldopen00203"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="adevice_8h_html"></a>
<a id="adevicetree_8h_html"></a>
<a id="aespi__emul_8h_html"></a>
<a id="agroup__devicetree-generic-foreach_html_ga926f68202042c9db05390e628787f916"></a>
<a id="agroup__io__emulators_html_ga39b7a9438507b0be95038fe9464762aa"></a>
<a id="agroup__io__emulators_html_gaa6129de6e0edef345242559a3dac3a50"></a>
<a id="agroup__io__emulators_html_gaad94c1e07998417cb9aa06d03be3b280"></a>
<a id="agroup__io__emulators_html_gad587b2852a182e1a7fdcb3b056d898f1"></a>
<a id="agroup__io__emulators_html_gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a"></a>
<a id="agroup__io__emulators_html_gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f"></a>
<a id="agroup__io__emulators_html_gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46"></a>
<a id="agroup__io__emulators_html_gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1"></a>
<a id="agroup__io__emulators_html_gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d"></a>
<a id="agroup__io__emulators_html_gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6"></a>
<a id="ai2c__emul_8h_html"></a>
<a id="amspi__emul_8h_html"></a>
<a id="aspi__emul_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructemul__link__for__bus_html"></a>
<a id="astructemul__link__for__bus_html_af81ff0873c340778030700d1cd2b7294"></a>
<a id="astructemul__list__for__bus_html"></a>
<a id="astructemul__list__for__bus_html_a4cd116abd8480895312564dcdf3f2e03"></a>
<a id="astructemul__list__for__bus_html_abcfe7bc6d82a16959c3d89b8598a8563"></a>
<a id="astructemul_html"></a>
<a id="astructemul_html_a4159ce815a6b4022bf35cbd0d0102bba"></a>
<a id="astructemul_html_a5ec4e292613d2d79d6bd57fe6cd5b41b"></a>
<a id="astructemul_html_a82f3fcaf221cd329ef1b6cb93cc7c8e6"></a>
<a id="astructemul_html_a92a4811a8656b8f0c3f3c7873918da3c"></a>
<a id="astructemul_html_a9f3ec93d05fdf287069dbb0aa48cc8ac"></a>
<a id="astructemul_html_ac7e90a7ff00a0c08836821c7d49b7dea"></a>
<a id="astructemul_html_ae6f86e44a6b28296528d607124f4b812"></a>
<a id="astructespi__emul_html"></a>
<a id="astructi2c__emul_html"></a>
<a id="astructmspi__emul_html"></a>
<a id="astructno__bus__emul_html"></a>
<a id="astructno__bus__emul_html_a9d4274ae11784a6c6e9892b1bde89780"></a>
<a id="astructno__bus__emul_html_aee2b4297901108a071658fa07e56043f"></a>
<a id="astructspi__emul_html"></a>
<a id="astructuart__emul_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="auart__emul_8h_html"></a>
<a id="aunionemul_1_1bus_html"></a>
<a id="aunionemul_1_1bus_html_a1f2079251cce4ffa92d3f1a4315b7b42"></a>
<a id="aunionemul_1_1bus_html_a4201a6d0980f539343936df40a5f7ca9"></a>
<a id="aunionemul_1_1bus_html_a6a8ad4e1e183a81c05b64b5c87cfa25a"></a>
<a id="aunionemul_1_1bus_html_aa9e71864d3e4a0df64ed785522f29139"></a>
<a id="aunionemul_1_1bus_html_ab88888ce5358ad5fa016cc5fe01ed98c"></a>
<a id="aunionemul_1_1bus_html_adbf407e15fbfe3da70b0c458e8edcf8d"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 * Copyright 2020 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_EMUL_H_


struct emul;

/* #includes required after forward-declaration of struct emul later defined in this header. */
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/drivers/espi_emul.h>
#include <zephyr/drivers/i2c_emul.h>
#include <zephyr/drivers/spi_emul.h>
#include <zephyr/drivers/mspi_emul.h>
#include <zephyr/drivers/uart_emul.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

enum emul_bus_type {
        EMUL_BUS_TYPE_I2C,
        EMUL_BUS_TYPE_ESPI,
        EMUL_BUS_TYPE_SPI,
        EMUL_BUS_TYPE_MSPI,
        EMUL_BUS_TYPE_UART,
        EMUL_BUS_TYPE_NONE,
};

struct emul_link_for_bus {
        const struct device *dev;
};

struct emul_list_for_bus {
        const struct emul_link_for_bus *children;
        unsigned int num_children;
};

typedef int (*emul_init_t)(const struct emul *emul, const struct device *parent);

struct no_bus_emul {
        void *api;
        uint16_t addr;
};

struct emul {
        emul_init_t init;
        const struct device *dev;
        const void *cfg;
        void *data;
        enum emul_bus_type bus_type;
        union bus {
                struct i2c_emul *i2c;
                struct espi_emul *espi;
                struct spi_emul *spi;
                struct mspi_emul *mspi;
                struct uart_emul *uart;
                struct no_bus_emul *none;
        } bus;

        const void *backend_api;
};

#define EMUL_DT_NAME_GET(node_id) _CONCAT(__emulreg_, node_id)

/* Get a unique identifier based on the given _dev_node_id's reg property and
 * the bus its on. Intended for use in other internal macros when declaring {bus}_emul
 * structs in peripheral emulators.
 */
#define Z_EMUL_REG_BUS_IDENTIFIER(_dev_node_id) _CONCAT(_CONCAT(__emulreg_, _dev_node_id), _bus)

/* Conditionally places text based on what bus _dev_node_id is on. */
#define Z_EMUL_BUS(_dev_node_id, _i2c, _espi, _spi, _mspi, _uart, _none)                           \
        COND_CASE_1(DT_ON_BUS(_dev_node_id, i2c), (_i2c),                                          \
                    DT_ON_BUS(_dev_node_id, espi), (_espi),                                        \
                    DT_ON_BUS(_dev_node_id, spi), (_spi),                                          \
                    DT_ON_BUS(_dev_node_id, mspi), (_mspi),                                        \
                    DT_ON_BUS(_dev_node_id, uart), (_uart),                                        \
                    (_none))

#define EMUL_DT_DEFINE(node_id, init_fn, data_ptr, cfg_ptr, bus_api, _backend_api)                 \
        static struct Z_EMUL_BUS(node_id, i2c_emul, espi_emul, spi_emul, mspi_emul, uart_emul,     \
                                 no_bus_emul) Z_EMUL_REG_BUS_IDENTIFIER(node_id) = {               \
                .api = bus_api,                                                                    \
                IF_ENABLED(DT_NODE_HAS_PROP(node_id, reg),                                         \
                           (.Z_EMUL_BUS(node_id, addr, chipsel, chipsel, dev_idx, dummy, addr) =   \
                                    DT_REG_ADDR(node_id),))};                                      \
        const STRUCT_SECTION_ITERABLE(emul, EMUL_DT_NAME_GET(node_id)) __used = {                  \
                .init = (init_fn),                                                                 \
                .dev = DEVICE_DT_GET(node_id),                                                     \
                .cfg = (cfg_ptr),                                                                  \
                .data = (data_ptr),                                                                \
                .bus_type = Z_EMUL_BUS(node_id, EMUL_BUS_TYPE_I2C, EMUL_BUS_TYPE_ESPI,             \
                                       EMUL_BUS_TYPE_SPI, EMUL_BUS_TYPE_MSPI, EMUL_BUS_TYPE_UART,  \
                                       EMUL_BUS_TYPE_NONE),                                        \
                .bus = {.Z_EMUL_BUS(node_id, i2c, espi, spi, mspi, uart, none) =                   \
                                &(Z_EMUL_REG_BUS_IDENTIFIER(node_id))},                            \
                .backend_api = (_backend_api),                                                     \
        };

#define EMUL_DT_INST_DEFINE(inst, ...) EMUL_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)

#define EMUL_DT_GET(node_id) (&EMUL_DT_NAME_GET(node_id))

#define EMUL_DT_GET_OR_NULL(node_id)                                                               \
        COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(node_id), (EMUL_DT_GET(node_id)), (NULL))

int emul_init_for_bus(const struct device *dev);

const struct emul *emul_get_binding(const char *name);



#define Z_MAYBE_EMUL_DECLARE_INTERNAL(node_id) extern const struct emul EMUL_DT_NAME_GET(node_id);

DT_FOREACH_STATUS_OKAY_NODE(Z_MAYBE_EMUL_DECLARE_INTERNAL);


#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif /* ZEPHYR_INCLUDE_DRIVERS_EMUL_H_ */
```

## 13.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

版权（Copyright）：2020 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

对本头文件中稍后定义的 `struct emul` 作前向声明之后，需要这些 `#include`。

### 注释 3：原第 38 行

条件编译标记：`__cplusplus`。

### 注释 4：原第 119 行

根据给定 `_dev_node_id` 的 `reg` 属性及其所在总线获取唯一标识符。预期供其他内部宏使用，在外设仿真器中声明 `{bus}_emul` 结构体。

### 注释 5：原第 125 行

根据 `_dev_node_id` 所在的总线有条件地放置文本。

### 注释 6：原第 243 行

条件编译标记：`__cplusplus`。

### 注释 7：原第 245 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_EMUL_H_`。

## 13.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [emul](../hardware/P477_仿真器实例结构.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/drivers/espi_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/espi__emul_8h.html)
- [zephyr/drivers/i2c_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/i2c__emul_8h.html)
- [zephyr/drivers/spi_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/spi__emul_8h.html)
- [zephyr/drivers/mspi_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi__emul_8h.html)
- [zephyr/drivers/uart_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/uart__emul_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [emul_bus_type](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#ga39b7a9438507b0be95038fe9464762aa)
- [EMUL_BUS_TYPE_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f)
- [EMUL_BUS_TYPE_ESPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1)
- [EMUL_BUS_TYPE_SPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a)
- [EMUL_BUS_TYPE_MSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46)
- [EMUL_BUS_TYPE_UART](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6)
- [EMUL_BUS_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)
- [emul_link_for_bus](../hardware/P478_总线仿真器链接结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](https://docs.zephyrproject.org/latest/doxygen/html/structemul__link__for__bus.html#af81ff0873c340778030700d1cd2b7294)
- [emul_list_for_bus](../hardware/P479_总线仿真器列表结构.md)
- [children](https://docs.zephyrproject.org/latest/doxygen/html/structemul__list__for__bus.html#a4cd116abd8480895312564dcdf3f2e03)
- [num_children](https://docs.zephyrproject.org/latest/doxygen/html/structemul__list__for__bus.html#abcfe7bc6d82a16959c3d89b8598a8563)
- [emul_init_t](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gaa6129de6e0edef345242559a3dac3a50)
- [no_bus_emul](../hardware/P480_无总线仿真器桩结构.md)
- [api](https://docs.zephyrproject.org/latest/doxygen/html/structno__bus__emul.html#a9d4274ae11784a6c6e9892b1bde89780)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structno__bus__emul.html#aee2b4297901108a071658fa07e56043f)
- [init](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a5ec4e292613d2d79d6bd57fe6cd5b41b)
- [dev](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a4159ce815a6b4022bf35cbd0d0102bba)
- [cfg](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ae6f86e44a6b28296528d607124f4b812)
- [data](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a82f3fcaf221cd329ef1b6cb93cc7c8e6)
- [bus_type](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a92a4811a8656b8f0c3f3c7873918da3c)
- [bus](../hardware/P485_仿真器总线联合体.md)
- [i2c_emul](../hardware/P316_I2C模拟设备节点.md)
- [i2c](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#a1f2079251cce4ffa92d3f1a4315b7b42)
- [espi_emul](../hardware/P488_eSPI仿真器链表节点.md)
- [espi](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#adbf407e15fbfe3da70b0c458e8edcf8d)
- [spi_emul](../hardware/P327_SPI模拟器结构.md)
- [spi](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#aa9e71864d3e4a0df64ed785522f29139)
- [mspi_emul](../hardware/P489_MSPI仿真器链表节点.md)
- [mspi](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#ab88888ce5358ad5fa016cc5fe01ed98c)
- [uart_emul](../hardware/P342_UART模拟器结构.md)
- [uart](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#a4201a6d0980f539343936df40a5f7ca9)
- [none](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#a6a8ad4e1e183a81c05b64b5c87cfa25a)
- [bus](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a9f3ec93d05fdf287069dbb0aa48cc8ac)
- [backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)
- [emul_init_for_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad587b2852a182e1a7fdcb3b056d898f1)
- [emul_get_binding](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gaad94c1e07998417cb9aa06d03be3b280)
- [DT_FOREACH_STATUS_OKAY_NODE](../dt_foreach_reference/P001_设备树遍历宏.md#ga926f68202042c9db05390e628787f916)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [espi_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/espi__emul_8h.html)
- [i2c_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/i2c__emul_8h.html)
- [mspi_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi__emul_8h.html)
- [spi_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/spi__emul_8h.html)
- [emul_link_for_bus::dev](https://docs.zephyrproject.org/latest/doxygen/html/structemul__link__for__bus.html#af81ff0873c340778030700d1cd2b7294)
- [emul_list_for_bus::children](https://docs.zephyrproject.org/latest/doxygen/html/structemul__list__for__bus.html#a4cd116abd8480895312564dcdf3f2e03)
- [emul_list_for_bus::num_children](https://docs.zephyrproject.org/latest/doxygen/html/structemul__list__for__bus.html#abcfe7bc6d82a16959c3d89b8598a8563)
- [emul::dev](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a4159ce815a6b4022bf35cbd0d0102bba)
- [emul::init](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a5ec4e292613d2d79d6bd57fe6cd5b41b)
- [emul::data](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a82f3fcaf221cd329ef1b6cb93cc7c8e6)
- [emul::bus_type](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a92a4811a8656b8f0c3f3c7873918da3c)
- [emul::bus](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a9f3ec93d05fdf287069dbb0aa48cc8ac)
- [emul::backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)
- [emul::cfg](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ae6f86e44a6b28296528d607124f4b812)
- [no_bus_emul::api](https://docs.zephyrproject.org/latest/doxygen/html/structno__bus__emul.html#a9d4274ae11784a6c6e9892b1bde89780)
- [no_bus_emul::addr](https://docs.zephyrproject.org/latest/doxygen/html/structno__bus__emul.html#aee2b4297901108a071658fa07e56043f)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [uart_emul.h](https://docs.zephyrproject.org/latest/doxygen/html/uart__emul_8h.html)
- [emul::bus](../hardware/P485_仿真器总线联合体.md)
- [emul::bus::i2c](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#a1f2079251cce4ffa92d3f1a4315b7b42)
- [emul::bus::uart](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#a4201a6d0980f539343936df40a5f7ca9)
- [emul::bus::none](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#a6a8ad4e1e183a81c05b64b5c87cfa25a)
- [emul::bus::spi](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#aa9e71864d3e4a0df64ed785522f29139)
- [emul::bus::mspi](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#ab88888ce5358ad5fa016cc5fe01ed98c)
- [emul::bus::espi](https://docs.zephyrproject.org/latest/doxygen/html/unionemul_1_1bus.html#adbf407e15fbfe3da70b0c458e8edcf8d)

---

[上一章](P012_dma_bee.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P014_battery.h_源码浏览.md)
