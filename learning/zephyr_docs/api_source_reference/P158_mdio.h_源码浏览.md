---
id: learning.zephyr-docs.api-source-reference.page-158
title: mdio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mdio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第158章\_mdio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mdio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mdio_8h.html)。

## 158.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00086"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__mdio__interface__backend_html_ga09e5f0532a3d88249ee6e852be45e434"></a>
<a id="agroup__mdio__interface__backend_html_ga98d32453b4b8ec4abb36113c54711570"></a>
<a id="agroup__mdio__interface__backend_html_gaba3f545bba5aa028f50c4a7f6e43abd0"></a>
<a id="agroup__mdio__interface__backend_html_gadd83bf9b8e4b4bd7189bc0b814c1f535"></a>
<a id="agroup__mdio__interface_html_ga6a18c3d67c6dc7ef1f3f0e3780015d48"></a>
<a id="agroup__mdio__interface_html_ga93e360a1201c2bb1ddd33b94e6fce619"></a>
<a id="agroup__mdio__interface_html_gad8868e94f7335fea3cd9fea338ef9bd5"></a>
<a id="agroup__mdio__interface_html_gae056ee61011eb6e8d68254680f918434"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructmdio__driver__api_html"></a>
<a id="astructmdio__driver__api_html_a37329cf08f4eb6a9e2ad36e987d4d329"></a>
<a id="astructmdio__driver__api_html_a95b8e08d326ea522e670c90e629b6c86"></a>
<a id="astructmdio__driver__api_html_ac5ad4a58e170d684416997f30c8ac8bb"></a>
<a id="astructmdio__driver__api_html_ae76af9e29b24d9840566d4659a001bdd"></a>

```c
/*
 * Copyright (c) 2021 IP-Logix Inc.
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MDIO_H_
#define ZEPHYR_INCLUDE_DRIVERS_MDIO_H_

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef int (*mdio_api_read_t)(const struct device *dev, uint8_t prtad, uint8_t regad,
                               uint16_t *data);

typedef int (*mdio_api_write_t)(const struct device *dev, uint8_t prtad, uint8_t regad,
                                uint16_t data);

typedef int (*mdio_api_read_c45_t)(const struct device *dev, uint8_t prtad, uint8_t devad,
                                   uint16_t regad, uint16_t *data);

typedef int (*mdio_api_write_c45_t)(const struct device *dev, uint8_t prtad, uint8_t devad,
                                    uint16_t regad, uint16_t data);

__subsystem struct mdio_driver_api {
        mdio_api_read_t read;

        mdio_api_write_t write;

        mdio_api_read_c45_t read_c45;

        mdio_api_write_c45_t write_c45;
};


__syscall int mdio_read(const struct device *dev, uint8_t prtad, uint8_t regad,
                        uint16_t *data);

static inline int z_impl_mdio_read(const struct device *dev, uint8_t prtad,
                                   uint8_t regad, uint16_t *data)
{
        if (DEVICE_API_GET(mdio, dev)->read == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(mdio, dev)->read(dev, prtad, regad, data);
}


__syscall int mdio_write(const struct device *dev, uint8_t prtad, uint8_t regad,
                         uint16_t data);

static inline int z_impl_mdio_write(const struct device *dev, uint8_t prtad,
                                    uint8_t regad, uint16_t data)
{
        if (DEVICE_API_GET(mdio, dev)->write == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(mdio, dev)->write(dev, prtad, regad, data);
}

__syscall int mdio_read_c45(const struct device *dev, uint8_t prtad,
                            uint8_t devad, uint16_t regad, uint16_t *data);

static inline int z_impl_mdio_read_c45(const struct device *dev, uint8_t prtad,
                                       uint8_t devad, uint16_t regad,
                                       uint16_t *data)
{
        if (DEVICE_API_GET(mdio, dev)->read_c45 == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(mdio, dev)->read_c45(dev, prtad, devad, regad, data);
}

__syscall int mdio_write_c45(const struct device *dev, uint8_t prtad,
                             uint8_t devad, uint16_t regad, uint16_t data);

static inline int z_impl_mdio_write_c45(const struct device *dev, uint8_t prtad,
                                        uint8_t devad, uint16_t regad,
                                        uint16_t data)
{
        if (DEVICE_API_GET(mdio, dev)->write_c45 == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(mdio, dev)->write_c45(dev, prtad, devad, regad, data);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/mdio.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_MDIO_H_ */
```

## 158.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 IP-Logix Inc.。

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 218 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MDIO_H_`。

## 158.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mdio_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [mdio_api_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#gadd83bf9b8e4b4bd7189bc0b814c1f535)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [mdio_api_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#ga09e5f0532a3d88249ee6e852be45e434)
- [mdio_api_read_c45_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#gaba3f545bba5aa028f50c4a7f6e43abd0)
- [mdio_api_write_c45_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#ga98d32453b4b8ec4abb36113c54711570)
- [mdio_driver_api](../network_service_model_reference/P030_mdio_driver_api_结构体.md)
- [read](../network_service_model_reference/P030_mdio_driver_api_结构体.md#a37329cf08f4eb6a9e2ad36e987d4d329)
- [write](../network_service_model_reference/P030_mdio_driver_api_结构体.md#ac5ad4a58e170d684416997f30c8ac8bb)
- [read_c45](../network_service_model_reference/P030_mdio_driver_api_结构体.md#ae76af9e29b24d9840566d4659a001bdd)
- [write_c45](../network_service_model_reference/P030_mdio_driver_api_结构体.md#a95b8e08d326ea522e670c90e629b6c86)
- [mdio_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#gae056ee61011eb6e8d68254680f918434)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [mdio_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#ga6a18c3d67c6dc7ef1f3f0e3780015d48)
- [mdio_read_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#ga93e360a1201c2bb1ddd33b94e6fce619)
- [mdio_write_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#gad8868e94f7335fea3cd9fea338ef9bd5)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [mdio_driver_api::read](../network_service_model_reference/P030_mdio_driver_api_结构体.md#a37329cf08f4eb6a9e2ad36e987d4d329)
- [mdio_driver_api::write_c45](../network_service_model_reference/P030_mdio_driver_api_结构体.md#a95b8e08d326ea522e670c90e629b6c86)
- [mdio_driver_api::write](../network_service_model_reference/P030_mdio_driver_api_结构体.md#ac5ad4a58e170d684416997f30c8ac8bb)
- [mdio_driver_api::read_c45](../network_service_model_reference/P030_mdio_driver_api_结构体.md#ae76af9e29b24d9840566d4659a001bdd)

---

[上一章](P157_devicetree.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P159_adp5360.h_源码浏览.md)
