---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-21
title: zephyr__drivers__peci.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/peci_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr__drivers__peci.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/peci_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P021_zephyr__drivers__peci.h_头文件参考.md)。

## 21.1\_原始可见代码（Source Code）

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
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00217"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="foldopen00231"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00250"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__peci__interface__backend_html_ga3addf7ae61d89626f7d8889910c6f5b9"></a>
<a id="agroup__peci__interface__backend_html_ga60a85f356ed8f18050f1a4cd02389c77"></a>
<a id="agroup__peci__interface__backend_html_ga97cd68ca4d0b79a6ff8fc19828e0cb76"></a>
<a id="agroup__peci__interface__backend_html_gabdb55d1aeea952970562c58f7c901361"></a>
<a id="agroup__peci__interface_html_ga76ad37d4317b48311cf23cf516549544"></a>
<a id="agroup__peci__interface_html_gaa1fee6839b68eed73f0a8d93b3a3ec82"></a>
<a id="agroup__peci__interface_html_gaa42e2e015a2c778a9eaf2dc1b697630f"></a>
<a id="agroup__peci__interface_html_gacd243f64973f7bdcc8c999dc14ed2bd6"></a>
<a id="agroup__peci__interface_html_gacf15bdae6483ad3e9498ed984a959687"></a>
<a id="agroup__peci__interface_html_gaf197262cd58db5eb7691d1ce816057de"></a>
<a id="agroup__peci__interface_html_gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41"></a>
<a id="agroup__peci__interface_html_gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f"></a>
<a id="agroup__peci__interface_html_gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158"></a>
<a id="agroup__peci__interface_html_ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructpeci__buf_html"></a>
<a id="astructpeci__buf_html_a8e3fd0ef3f9141113214b89bb589a5e9"></a>
<a id="astructpeci__buf_html_aca55975957106666161da358b7f85db6"></a>
<a id="astructpeci__driver__api_html"></a>
<a id="astructpeci__driver__api_html_a0ca94e90b589beb0ab525ee141be6b49"></a>
<a id="astructpeci__driver__api_html_a2adf7c329d2b95cea596e5639fbe9e09"></a>
<a id="astructpeci__driver__api_html_a718840a487a31212a042d36cbf3119c7"></a>
<a id="astructpeci__driver__api_html_ae41c38a71a700e8a5808218fbb639fcc"></a>
<a id="astructpeci__msg_html"></a>
<a id="astructpeci__msg_html_a0449f151c62e672553d7d60480e1b995"></a>
<a id="astructpeci__msg_html_a10b270f4669c85a85c6e8f1bef7671e8"></a>
<a id="astructpeci__msg_html_a22e435e110d261b8ecd5180d118ffd2d"></a>
<a id="astructpeci__msg_html_a2990d5a2ae318020ed9301dd2de37070"></a>
<a id="astructpeci__msg_html_aa4d6785fc79059dc7e8574010bc29e4c"></a>
<a id="astructpeci__msg_html_abea62e39ca0ac59fca47c2f08a72f1e8"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PECI_H_
#define ZEPHYR_INCLUDE_DRIVERS_PECI_H_


#include <errno.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

enum peci_error_code {
        PECI_GENERAL_SENSOR_ERROR    = 0x8000,
        PECI_UNDERFLOW_SENSOR_ERROR  = 0x8002,
        PECI_OVERFLOW_SENSOR_ERROR   = 0x8003,
};

enum peci_command_code {
        PECI_CMD_PING                = 0x00,
        PECI_CMD_GET_TEMP0           = 0x01,
        PECI_CMD_GET_TEMP1           = 0x02,
        PECI_CMD_RD_PCI_CFG0         = 0x61,
        PECI_CMD_RD_PCI_CFG1         = 0x62,
        PECI_CMD_WR_PCI_CFG0         = 0x65,
        PECI_CMD_WR_PCI_CFG1         = 0x66,
        PECI_CMD_RD_PKG_CFG0         = 0xA1,
        PECI_CMD_RD_PKG_CFG1         = 0xA2,
        PECI_CMD_WR_PKG_CFG0         = 0xA5,
        PECI_CMD_WR_PKG_CFG1         = 0xA6,
        PECI_CMD_RD_IAMSR0           = 0xB1,
        PECI_CMD_RD_IAMSR1           = 0xB2,
        PECI_CMD_WR_IAMSR0           = 0xB5,
        PECI_CMD_WR_IAMSR1           = 0xB6,
        PECI_CMD_RD_PCI_CFG_LOCAL0   = 0xE1,
        PECI_CMD_RD_PCI_CFG_LOCAL1   = 0xE2,
        PECI_CMD_WR_PCI_CFG_LOCAL0   = 0xE5,
        PECI_CMD_WR_PCI_CFG_LOCAL1   = 0xE6,
        PECI_CMD_GET_DIB             = 0xF7,
};

#define PECI_CC_RSP_SUCCESS              (0x40U)
#define PECI_CC_RSP_TIMEOUT              (0x80U)
#define PECI_CC_OUT_OF_RESOURCES_TIMEOUT (0x81U)
#define PECI_CC_RESOURCES_LOWPWR_TIMEOUT (0x82U)
#define PECI_CC_ILLEGAL_REQUEST          (0x90U)

#define PECI_PING_WR_LEN               (0U)
#define PECI_PING_RD_LEN               (0U)
#define PECI_PING_LEN                  (3U)

#define PECI_GET_DIB_WR_LEN            (1U)
#define PECI_GET_DIB_RD_LEN            (8U)
#define PECI_GET_DIB_CMD_LEN           (4U)
#define PECI_GET_DIB_DEVINFO           (0U)
#define PECI_GET_DIB_REVNUM            (1U)
#define PECI_GET_DIB_DOMAIN_BIT_MASK   (0x4U)
#define PECI_GET_DIB_MAJOR_REV_MASK    0xF0
#define PECI_GET_DIB_MINOR_REV_MASK    0x0F

#define PECI_GET_TEMP_WR_LEN           (1U)
#define PECI_GET_TEMP_RD_LEN           (2U)
#define PECI_GET_TEMP_CMD_LEN          (4U)
#define PECI_GET_TEMP_LSB              (0U)
#define PECI_GET_TEMP_MSB              (1U)
#define PECI_GET_TEMP_ERR_MSB          (0x80U)
#define PECI_GET_TEMP_ERR_LSB_GENERAL  (0x0U)
#define PECI_GET_TEMP_ERR_LSB_RES      (0x1U)
#define PECI_GET_TEMP_ERR_LSB_TEMP_LO  (0x2U)
#define PECI_GET_TEMP_ERR_LSB_TEMP_HI  (0x3U)

#define PECI_RD_PKG_WR_LEN             (5U)
#define PECI_RD_PKG_LEN_BYTE           (2U)
#define PECI_RD_PKG_LEN_WORD           (3U)
#define PECI_RD_PKG_LEN_DWORD          (5U)
#define PECI_RD_PKG_CMD_LEN            (8U)

#define PECI_WR_PKG_RD_LEN              (1U)
#define PECI_WR_PKG_LEN_BYTE            (7U)
#define PECI_WR_PKG_LEN_WORD            (8U)
#define PECI_WR_PKG_LEN_DWORD           (10U)
#define PECI_WR_PKG_CMD_LEN             (9U)

#define PECI_RD_IAMSR_WR_LEN            (5U)
#define PECI_RD_IAMSR_LEN_BYTE          (2U)
#define PECI_RD_IAMSR_LEN_WORD          (3U)
#define PECI_RD_IAMSR_LEN_DWORD         (5U)
#define PECI_RD_IAMSR_LEN_QWORD         (9U)
#define PECI_RD_IAMSR_CMD_LEN           (8U)

#define PECI_WR_IAMSR_RD_LEN            (1U)
#define PECI_WR_IAMSR_LEN_BYTE          (7U)
#define PECI_WR_IAMSR_LEN_WORD          (8U)
#define PECI_WR_IAMSR_LEN_DWORD         (10U)
#define PECI_WR_IAMSR_LEN_QWORD         (14U)
#define PECI_WR_IAMSR_CMD_LEN           (9U)

#define PECI_RD_PCICFG_WR_LEN           (6U)
#define PECI_RD_PCICFG_LEN_BYTE         (2U)
#define PECI_RD_PCICFG_LEN_WORD         (3U)
#define PECI_RD_PCICFG_LEN_DWORD        (5U)
#define PECI_RD_PCICFG_CMD_LEN          (9U)

#define PECI_WR_PCICFG_RD_LEN           (1U)
#define PECI_WR_PCICFG_LEN_BYTE         (8U)
#define PECI_WR_PCICFG_LEN_WORD         (9U)
#define PECI_WR_PCICFG_LEN_DWORD        (11U)
#define PECI_WR_PCICFG_CMD_LEN          (10U)

#define PECI_RD_PCICFGL_WR_LEN          (5U)
#define PECI_RD_PCICFGL_RD_LEN_BYTE     (2U)
#define PECI_RD_PCICFGL_RD_LEN_WORD     (3U)
#define PECI_RD_PCICFGL_RD_LEN_DWORD    (5U)
#define PECI_RD_PCICFGL_CMD_LEN         (8U)

#define PECI_WR_PCICFGL_RD_LEN          (1U)
#define PECI_WR_PCICFGL_WR_LEN_BYTE     (7U)
#define PECI_WR_PCICFGL_WR_LEN_WORD     (8U)
#define PECI_WR_PCICFGL_WR_LEN_DWORD    (10U)
#define PECI_WR_PCICFGL_CMD_LEN         (9U)

struct peci_buf {
        uint8_t *buf;
        size_t len;
};

struct peci_msg {
        uint8_t addr;
        enum peci_command_code cmd_code;
        struct peci_buf tx_buffer;
        struct peci_buf rx_buffer;
        uint8_t oob_addr;
        uint8_t flags;
};


typedef int (*peci_config_t)(const struct device *dev, uint32_t bitrate);

typedef int (*peci_transfer_t)(const struct device *dev, struct peci_msg *msg);

typedef int (*peci_disable_t)(const struct device *dev);

typedef int (*peci_enable_t)(const struct device *dev);

__subsystem struct peci_driver_api {
        peci_config_t config;
        peci_disable_t disable;
        peci_enable_t enable;
        peci_transfer_t transfer;
};


__syscall int peci_config(const struct device *dev, uint32_t bitrate);

static inline int z_impl_peci_config(const struct device *dev,
                                     uint32_t bitrate)
{
        return DEVICE_API_GET(peci, dev)->config(dev, bitrate);
}

__syscall int peci_enable(const struct device *dev);

static inline int z_impl_peci_enable(const struct device *dev)
{
        return DEVICE_API_GET(peci, dev)->enable(dev);
}

__syscall int peci_disable(const struct device *dev);

static inline int z_impl_peci_disable(const struct device *dev)
{
        return DEVICE_API_GET(peci, dev)->disable(dev);
}


__syscall int peci_transfer(const struct device *dev, struct peci_msg *msg);

static inline int z_impl_peci_transfer(const struct device *dev,
                                       struct peci_msg *msg)
{
        return DEVICE_API_GET(peci, dev)->transfer(dev, msg);
}


#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/peci.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_PECI_H_ */
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 363 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PECI_H_`。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P021_zephyr__drivers__peci.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [peci_error_code](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga76ad37d4317b48311cf23cf516549544)
- [PECI_GENERAL_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f)
- [PECI_UNDERFLOW_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41)
- [PECI_OVERFLOW_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2)
- [peci_command_code](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacd243f64973f7bdcc8c999dc14ed2bd6)
- [PECI_CMD_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d)
- [PECI_CMD_GET_TEMP0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf)
- [PECI_CMD_GET_TEMP1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c)
- [PECI_CMD_RD_PCI_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d)
- [PECI_CMD_RD_PCI_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa)
- [PECI_CMD_WR_PCI_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc)
- [PECI_CMD_WR_PCI_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12)
- [PECI_CMD_RD_PKG_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523)
- [PECI_CMD_RD_PKG_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed)
- [PECI_CMD_WR_PKG_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55)
- [PECI_CMD_WR_PKG_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95)
- [PECI_CMD_RD_IAMSR0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10)
- [PECI_CMD_RD_IAMSR1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53)
- [PECI_CMD_WR_IAMSR0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2)
- [PECI_CMD_WR_IAMSR1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3)
- [PECI_CMD_RD_PCI_CFG_LOCAL0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5)
- [PECI_CMD_RD_PCI_CFG_LOCAL1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c)
- [PECI_CMD_WR_PCI_CFG_LOCAL0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158)
- [PECI_CMD_WR_PCI_CFG_LOCAL1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd)
- [PECI_CMD_GET_DIB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8)
- [peci_buf](../peripheral_bus_storage_model_reference/P066_peci_buf_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [buf](../peripheral_bus_storage_model_reference/P066_peci_buf_结构体.md#aca55975957106666161da358b7f85db6)
- [len](../peripheral_bus_storage_model_reference/P066_peci_buf_结构体.md#a8e3fd0ef3f9141113214b89bb589a5e9)
- [peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)
- [addr](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#aa4d6785fc79059dc7e8574010bc29e4c)
- [cmd_code](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#a10b270f4669c85a85c6e8f1bef7671e8)
- [tx_buffer](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#a22e435e110d261b8ecd5180d118ffd2d)
- [rx_buffer](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#abea62e39ca0ac59fca47c2f08a72f1e8)
- [oob_addr](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#a2990d5a2ae318020ed9301dd2de37070)
- [flags](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#a0449f151c62e672553d7d60480e1b995)
- [peci_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#gabdb55d1aeea952970562c58f7c901361)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [peci_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga3addf7ae61d89626f7d8889910c6f5b9)
- [peci_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga97cd68ca4d0b79a6ff8fc19828e0cb76)
- [peci_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga60a85f356ed8f18050f1a4cd02389c77)
- [peci_driver_api](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md)
- [config](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md#ae41c38a71a700e8a5808218fbb639fcc)
- [disable](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md#a718840a487a31212a042d36cbf3119c7)
- [enable](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md#a2adf7c329d2b95cea596e5639fbe9e09)
- [transfer](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md#a0ca94e90b589beb0ab525ee141be6b49)
- [peci_config](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa1fee6839b68eed73f0a8d93b3a3ec82)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [peci_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa42e2e015a2c778a9eaf2dc1b697630f)
- [peci_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaf197262cd58db5eb7691d1ce816057de)
- [peci_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacf15bdae6483ad3e9498ed984a959687)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [peci_buf::len](../peripheral_bus_storage_model_reference/P066_peci_buf_结构体.md#a8e3fd0ef3f9141113214b89bb589a5e9)
- [peci_buf::buf](../peripheral_bus_storage_model_reference/P066_peci_buf_结构体.md#aca55975957106666161da358b7f85db6)
- [peci_driver_api::transfer](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md#a0ca94e90b589beb0ab525ee141be6b49)
- [peci_driver_api::enable](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md#a2adf7c329d2b95cea596e5639fbe9e09)
- [peci_driver_api::disable](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md#a718840a487a31212a042d36cbf3119c7)
- [peci_driver_api::config](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md#ae41c38a71a700e8a5808218fbb639fcc)
- [peci_msg::flags](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#a0449f151c62e672553d7d60480e1b995)
- [peci_msg::cmd_code](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#a10b270f4669c85a85c6e8f1bef7671e8)
- [peci_msg::tx_buffer](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#a22e435e110d261b8ecd5180d118ffd2d)
- [peci_msg::oob_addr](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#a2990d5a2ae318020ed9301dd2de37070)
- [peci_msg::addr](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#aa4d6785fc79059dc7e8574010bc29e4c)
- [peci_msg::rx_buffer](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md#abea62e39ca0ac59fca47c2f08a72f1e8)

---

[上一章](P020_zephyr__mgmt__osdp.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__ps2.h_头文件源码.md)
