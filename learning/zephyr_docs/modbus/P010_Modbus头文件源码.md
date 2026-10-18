---
id: learning.zephyr-docs.modbus.api-10
title: Modbus头文件源码
kind: reference
status: maintained
domains: [zephyr, modbus, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modbus_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Modbus头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/modbus_8h_source.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 10.1\_阅读说明

[返回头文件参考](P009_Modbus头文件参考.md)。

译注：下面保留官方Doxygen源码浏览页显示的代码。网页行号属于展示内容，已移除；显示用的不换行空格还原为普通空格，并清除空行尾部空白。原页本身省略了用于生成API文档的部分注释，因此原网页行号存在跳跃。此页不是另行抓取的完整原始头文件，接口注释的中文内容见[完整API参考](P008_Modbus完整API参考.md)及各结构体译页。标识符、宏、类型、函数声明及版权／许可注释保持原样。

## 10.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
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
<a id="l00028"></a>
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
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00457"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00472"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00484"></a>
<a id="l00486"></a>
<a id="l00492"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00505"></a>
<a id="l00507"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00515"></a>
<a id="l00517"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00526"></a>
<a id="l00528"></a>
<a id="l00530"></a>
<a id="l00532"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00653"></a>
<a id="l00654"></a>

```c
/*
 * Copyright (c) 2020 PHYTEC Messtechnik GmbH
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * Client API in this file is based on mbm_core.c from uC/Modbus Stack.
 *
 *                                uC/Modbus
 *                         The Embedded Modbus Stack
 *
 *      Copyright 2003-2020 Silicon Laboratories Inc. www.silabs.com
 *
 *                   SPDX-License-Identifier: Apache-2.0
 *
 * This software is subject to an open source license and is distributed by
 *  Silicon Laboratories Inc. pursuant to the terms of the Apache License,
 *      Version 2.0 available at www.apache.org/licenses/LICENSE-2.0.
 */



#ifndef ZEPHYR_INCLUDE_MODBUS_MODBUS_H_
#define ZEPHYR_INCLUDE_MODBUS_MODBUS_H_

#include <zephyr/drivers/uart.h>
#include <zephyr/sys/slist.h>
#ifdef __cplusplus
extern "C" {
#endif

#define MODBUS_MBAP_LENGTH              7
#define MODBUS_MBAP_AND_FC_LENGTH       (MODBUS_MBAP_LENGTH + 1)

#define MODBUS_EXC_NONE                         0
#define MODBUS_EXC_ILLEGAL_FC                   1
#define MODBUS_EXC_ILLEGAL_DATA_ADDR            2
#define MODBUS_EXC_ILLEGAL_DATA_VAL             3
#define MODBUS_EXC_SERVER_DEVICE_FAILURE        4
#define MODBUS_EXC_ACK                          5
#define MODBUS_EXC_SERVER_DEVICE_BUSY           6
#define MODBUS_EXC_MEM_PARITY_ERROR             8
#define MODBUS_EXC_GW_PATH_UNAVAILABLE          10
#define MODBUS_EXC_GW_TARGET_FAILED_TO_RESP     11

struct modbus_adu {
        uint16_t trans_id;
        uint16_t proto_id;
        uint16_t length;
        uint8_t unit_id;
        uint8_t fc;
        uint8_t data[CONFIG_MODBUS_BUFFER_SIZE - 4];
        uint16_t crc;
};

int modbus_read_coils(const int iface,
                      const uint8_t unit_id,
                      const uint16_t start_addr,
                      uint8_t *const coil_tbl,
                      const uint16_t num_coils);

int modbus_read_dinputs(const int iface,
                        const uint8_t unit_id,
                        const uint16_t start_addr,
                        uint8_t *const di_tbl,
                        const uint16_t num_di);

int modbus_read_holding_regs(const int iface,
                             const uint8_t unit_id,
                             const uint16_t start_addr,
                             uint16_t *const reg_buf,
                             const uint16_t num_regs);

int modbus_read_input_regs(const int iface,
                           const uint8_t unit_id,
                           const uint16_t start_addr,
                           uint16_t *const reg_buf,
                           const uint16_t num_regs);

int modbus_write_coil(const int iface,
                      const uint8_t unit_id,
                      const uint16_t coil_addr,
                      const bool coil_state);

int modbus_write_holding_reg(const int iface,
                             const uint8_t unit_id,
                             const uint16_t start_addr,
                             const uint16_t reg_val);

int modbus_request_diagnostic(const int iface,
                              const uint8_t unit_id,
                              const uint16_t sfunc,
                              const uint16_t data,
                              uint16_t *const data_out);

int modbus_write_coils(const int iface,
                       const uint8_t unit_id,
                       const uint16_t start_addr,
                       uint8_t *const coil_tbl,
                       const uint16_t num_coils);

int modbus_write_holding_regs(const int iface,
                              const uint8_t unit_id,
                              const uint16_t start_addr,
                              uint16_t *const reg_buf,
                              const uint16_t num_regs);

int modbus_read_holding_regs_fp(const int iface,
                                const uint8_t unit_id,
                                const uint16_t start_addr,
                                float *const reg_buf,
                                const uint16_t num_regs);

int modbus_write_holding_regs_fp(const int iface,
                                 const uint8_t unit_id,
                                 const uint16_t start_addr,
                                 float *const reg_buf,
                                 const uint16_t num_regs);

struct modbus_user_callbacks {
        int (*coil_rd)(uint16_t addr, bool *state);

        int (*coil_wr)(uint16_t addr, bool state);

        int (*discrete_input_rd)(uint16_t addr, bool *state);

        int (*input_reg_rd)(uint16_t addr, uint16_t *reg);

        int (*input_reg_rd_fp)(uint16_t addr, float *reg);

        int (*holding_reg_rd)(uint16_t addr, uint16_t *reg);

        int (*holding_reg_wr)(uint16_t addr, uint16_t reg);

        int (*holding_reg_rd_fp)(uint16_t addr, float *reg);

        int (*holding_reg_wr_fp)(uint16_t addr, float reg);
};

int modbus_iface_get_by_name(const char *iface_name);

typedef int (*modbus_raw_cb_t)(const int iface, const struct modbus_adu *adu,
                                void *user_data);

typedef bool (*modbus_custom_cb_t)(const int iface,
                                const struct modbus_adu *const rx_adu,
                                struct modbus_adu *const tx_adu,
                                uint8_t *const excep_code,
                                void *const user_data);

struct modbus_custom_fc {
        sys_snode_t node;
        modbus_custom_cb_t cb;
        void *user_data;
        uint8_t fc;
        uint8_t excep_code;
};

#define MODBUS_CUSTOM_FC_DEFINE(name, user_cb, user_fc, userdata)       \
        static struct modbus_custom_fc modbus_cfg_##name = {            \
                .cb = user_cb,                                          \
                .user_data = userdata,                                  \
                .fc = user_fc,                                          \
                .excep_code = MODBUS_EXC_NONE,                          \
        }

enum modbus_mode {
        MODBUS_MODE_RTU,
        MODBUS_MODE_ASCII,
        MODBUS_MODE_RAW,
};

struct modbus_serial_param {
        uint32_t baud;
        enum uart_config_parity parity;
        enum uart_config_stop_bits stop_bits;
};

struct modbus_server_param {
        struct modbus_user_callbacks *user_cb;
        uint8_t unit_id;
};

struct modbus_raw_cb {
        modbus_raw_cb_t raw_tx_cb;
        void *user_data;
};

struct modbus_iface_param {
        enum modbus_mode mode;
        union {
                struct modbus_server_param server;
                uint32_t rx_timeout;
        };
        union {
                struct modbus_serial_param serial;
                struct modbus_raw_cb rawcb;
        };
};

int modbus_init_server(const int iface, struct modbus_iface_param param);

int modbus_init_client(const int iface, struct modbus_iface_param param);

int modbus_disable(const uint8_t iface);

int modbus_raw_submit_rx(const int iface, const struct modbus_adu *adu);

void modbus_raw_put_header(const struct modbus_adu *adu, uint8_t *header);

void modbus_raw_get_header(struct modbus_adu *adu, const uint8_t *header);

void modbus_raw_set_server_failure(struct modbus_adu *adu);

int modbus_raw_backend_txn(const int iface, struct modbus_adu *adu);

int modbus_register_user_fc(const int iface, struct modbus_custom_fc *custom_fc);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MODBUS_MODBUS_H_ */
```

## 10.3\_源码注释译文

开头版权注释：2020年PHYTEC Messtechnik GmbH；2021年Nordic Semiconductor ASA。SPDX许可标识符（License Identifier）为`Apache-2.0`。

本文件中的客户端API以uC/Modbus协议栈（uC/Modbus Stack）的`mbm_core.c`为基础。uC/Modbus的副标题是“嵌入式Modbus协议栈”（The Embedded Modbus Stack）。版权归Silicon Laboratories Inc.所有，年份为2003—2020，网站为`www.silabs.com`。

该软件受开源许可证约束，由Silicon Laboratories Inc.按Apache许可证2.0版（Apache License, Version 2.0）条款分发；原注释中的许可地址为`www.apache.org/licenses/LICENSE-2.0`。法律名称、署名和原始英文声明已在代码中完整保留。

文件末尾的`#endif`注释标明它结束头文件包含保护（Header Include Guard）`ZEPHYR_INCLUDE_MODBUS_MODBUS_H_`。

[上一章](P009_Modbus头文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_Modbus应用数据单元.md)
