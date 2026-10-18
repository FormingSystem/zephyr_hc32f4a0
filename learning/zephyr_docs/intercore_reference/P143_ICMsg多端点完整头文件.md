---
id: learning.zephyr-docs.intercore_reference.icmsgref-143
title: ICMsg多端点完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icmsg__me_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第143章\_ICMsg多端点完整头文件

原文：[icmsg__me_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/icmsg__me_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方`zephyr/ipc/icmsg_me.h`源码浏览页的完整可见代码。ICMsg 是核间消息传递（Inter-core Messaging）库，ME 指多端点扩展（Multi-endpoint Extension），IPC 指处理器间通信（Inter-Processor Communication）。展示行号已移除，原声明、注释、版权和许可证保留。

`icmsg_me_ept_id_t`是端点标识类型，底层为8位无符号整数`uint8_t`。端点槽位数组和发送缓冲区长度分别由 Kconfig 配置项`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_NUM_EP`和`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_SEND_BUF_SIZE`给出；Kconfig 是 Zephyr 的配置系统。

## 143.1\_完整可见源码

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IPC_ICMSG_ME_H_
#define ZEPHYR_INCLUDE_IPC_ICMSG_ME_H_

#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/ipc/icmsg.h>
#include <zephyr/ipc/ipc_service.h>

#ifdef __cplusplus
extern "C" {
#endif



/* If more bytes than 1 was used for endpoint id, endianness should be
 * considered.
 */
typedef uint8_t icmsg_me_ept_id_t;

struct icmsg_me_data_t {
        struct icmsg_data_t icmsg_data;
        struct ipc_ept_cfg ept_cfg;

        struct k_event event;

        struct k_mutex send_mutex;
        const struct ipc_ept_cfg *epts[CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_NUM_EP];

        uint8_t send_buffer[CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_SEND_BUF_SIZE] __aligned(4);
};


int icmsg_me_init(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data);

int icmsg_me_open(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data,
                  const struct ipc_service_cb *cb,
                  void *ctx);

void icmsg_me_wait_for_icmsg_bind(struct icmsg_me_data_t *data);

void icmsg_me_icmsg_bound(struct icmsg_me_data_t *data);

void icmsg_me_received_data(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                            const void *msg, size_t len);

int icmsg_me_set_empty_ept_cfg_slot(struct icmsg_me_data_t *data,
                                    const struct ipc_ept_cfg *ept_cfg,
                                    icmsg_me_ept_id_t *id);

int icmsg_me_set_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                         const struct ipc_ept_cfg *ept_cfg);

int icmsg_me_get_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                         const struct ipc_ept_cfg **ept_cfg);

void icmsg_me_reset_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id);

int icmsg_me_send(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                  const void *msg, size_t len);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_IPC_ICMSG_ME_H_ */
```

## 143.2\_可见注释与阅读说明

原文件版权为2023年 Nordic Semiconductor ASA，许可证为 Apache-2.0。头文件保护宏（Header Guard）为`ZEPHYR_INCLUDE_IPC_ICMSG_ME_H_`；`__cplusplus`与`extern "C"`用于保持 C++ 环境下的 C 语言链接方式。文件末尾注释标识保护宏结束。

端点标识类型前的原注释说明：**如果端点标识使用超过1字节，就应考虑字节序（Endianness）**。当前原声明仍为`uint8_t`。发送缓冲区的`__aligned(4)`指定4字节对齐，未在翻译中删除。

官方 Doxygen 已提取到说明页的文档注释见[多端点接口](P140_ICMsg多端点接口.md)，六个结构成员见[多端点运行时结构](P141_ICMsg多端点运行时结构.md)。

---

[上一章：ICMsg多端点头文件参考](P142_ICMsg多端点头文件参考.md) · [下一章：核间数据包缓冲区接口](P144_核间数据包缓冲区接口.md) · [返回大纲](大纲.md)
