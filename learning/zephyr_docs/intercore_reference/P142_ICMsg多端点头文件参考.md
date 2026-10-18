---
id: learning.zephyr-docs.intercore_reference.icmsgref-142
title: ICMsg多端点头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icmsg__me_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第142章\_ICMsg多端点头文件参考

原文：[icmsg__me_8h](https://docs.zephyrproject.org/latest/doxygen/html/icmsg__me_8h.html)。读取日期：2026-10-13，`latest`。

本页是 ICMsg 核间消息传递（Inter-core Messaging）多端点扩展（Multi-endpoint Extension，ME）头文件`zephyr/ipc/icmsg_me.h`的参考索引。

## 142.1\_包含文件


```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/ipc/icmsg.h>
#include <zephyr/ipc/ipc_service.h>
```

## 142.2\_运行时结构与端点标识

多端点运行时结构为[`icmsg_me_data_t`](P141_ICMsg多端点运行时结构.md)。端点标识（Endpoint ID）类型如下，`uint8_t`为8位无符号整数：

```c
typedef uint8_t icmsg_me_ept_id_t;
```

## 142.3\_函数声明

初始化多端点实例。

```c
int icmsg_me_init(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data);
```

打开多端点实例。

```c
int icmsg_me_open(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data,
                  const struct ipc_service_cb *cb,
                  void *ctx);
```

等待底层绑定。

```c
void icmsg_me_wait_for_icmsg_bind(struct icmsg_me_data_t *data);
```

通知底层已绑定。

```c
void icmsg_me_icmsg_bound(struct icmsg_me_data_t *data);
```

分发收到的数据。

```c
void icmsg_me_received_data(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                            const void *msg, size_t len);
```

选择空槽位并设置配置。

```c
int icmsg_me_set_empty_ept_cfg_slot(struct icmsg_me_data_t *data,
                                    const struct ipc_ept_cfg *ept_cfg,
                                    icmsg_me_ept_id_t *id);
```

设置指定槽位配置。

```c
int icmsg_me_set_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                         const struct ipc_ept_cfg *ept_cfg);
```

取得指定槽位配置。

```c
int icmsg_me_get_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                         const struct ipc_ept_cfg **ept_cfg);
```

清空指定槽位配置。

```c
void icmsg_me_reset_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id);
```

发送端点消息。

```c
int icmsg_me_send(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                  const void *msg, size_t len);
```

完整参数、返回值、回调转发责任与单实例不可重入要求见[多端点接口](P140_ICMsg多端点接口.md)；完整可见代码见[头文件源码](P143_ICMsg多端点完整头文件.md)。

---

[上一章：ICMsg多端点运行时结构](P141_ICMsg多端点运行时结构.md) · [下一章：ICMsg多端点完整头文件](P143_ICMsg多端点完整头文件.md) · [返回大纲](大纲.md)
