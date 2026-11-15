---
id: learning.zephyr-docs.intercore_reference.ipcguide-92
title: IPC服务使用指南
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/services/ipc/ipc_service/ipc_service.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第92章\_IPC服务使用指南

原文：[IPC service](https://docs.zephyrproject.org/latest/services/ipc/ipc_service/ipc_service.html)。读取日期：2026-10-13，`latest`。

处理器间通信（Inter-Processor Communication，IPC）服务应用程序编程接口（Application Programming Interface，API）用于在两个域（Domain）或中央处理器（Central Processing Unit，CPU）之间交换数据。

## 92.1\_实例与端点

一个IPC服务通信通道由一个实例（Instance）及其关联的一个或多个端点（Endpoint）组成。实例是两个域或CPU之间物理通信通道的外部表示，其内部表示与具体实现由后端（Backend）决定。

实例本身不用来发送数据；用户必须在实例中创建、注册端点，才能连接两个目标域并收发数据。单个实例可以有零个或多个端点，端点也可能具有不同优先级。端点优先级和多实例支持高度依赖所用后端。端点始终隶属于一个实例，是用户实际收发数据的对象。

实例通常由后端在初始化时（Init Time）创建，端点通常由用户在运行时（Run Time）注册。API不强制规定后端怎样创建实例，但强烈建议从设备树（Devicetree）取得实例配置。当前每个后端定义自己的设备树兼容配置，在启动时据此配置接口。

服务支持普通数据交换，以及使用无拷贝接口（No-copy API）的数据交换。

## 92.2\_普通数据交换

原代码使用`DEVICE_DT_GET`设备获取宏和`DT_NODELABEL`节点标签宏取得设备；后一个无拷贝例中的`K_FOREVER`是一直等待的超时常量。

必须先调用打开实例函数`ipc_service_open_instance()`打开实例，再将端点注册到该实例，然后发送数据。原示例：

```c
#include <zephyr/ipc/ipc_service.h>

static void bound_cb(void *priv)
{
   /* Endpoint bounded */
}

static void recv_cb(const void *data, size_t len, void *priv)
{
   /* Data received */
}

static struct ipc_ept_cfg ept0_cfg = {
   .name = "ept0",
   .cb = {
      .bound    = bound_cb,
      .received = recv_cb,
   },
};

int main(void)
{
   const struct device *inst0;
   struct ipc_ept ept0;
   int ret;

   inst0 = DEVICE_DT_GET(DT_NODELABEL(ipc0));
   ret = ipc_service_open_instance(inst0);
   ret = ipc_service_register_endpoint(inst0, &ept0, &ept0_cfg);

   /* Wait for endpoint bound (bound_cb called) */

   unsigned char message[] = "hello world";
   ret = ipc_service_send(&ept0, &message, sizeof(message));
}
```

原注释分别表示“端点已绑定”“数据已收到”以及“等待端点绑定，即`bound_cb`被调用”。`ipc_ept_cfg`为端点配置结构，`ipc_ept`为端点对象；`DEVICE_DT_GET(DT_NODELABEL(ipc0))`按设备树节点标签取得实例设备。

**示例译注：**原代码用注释标出等待绑定的位置，没有给出实际等待逻辑，也未逐次处理`ret`错误值。这里保留原示例，不把注释视为已经实现了等待。

## 92.3\_无拷贝数据交换

当后端支持无拷贝API时，可以直接读写共享内存（Shared Memory）区域：

```c
#include <zephyr/ipc/ipc_service.h>
#include <stdint.h>
#include <string.h>

static struct ipc_ept ept0;

static void bound_cb(void *priv)
{
   /* Endpoint bounded */
}

static void recv_cb_nocopy(const void *data, size_t len, void *priv)
{
   int ret;

   ret = ipc_service_hold_rx_buffer(&ept0, (void *)data);
   /* Process directly or put the buffer somewhere else and release. */
   ret = ipc_service_release_rx_buffer(&ept0, (void *)data);
}

static struct ipc_ept_cfg ept0_cfg = {
   .name = "ept0",
   .cb = {
      .bound    = bound_cb,
      .received = recv_cb,
   },
};

int main(void)
{
   const struct device *inst0;
   int ret;

   inst0 = DEVICE_DT_GET(DT_NODELABEL(ipc0));
   ret = ipc_service_open_instance(inst0);
   ret = ipc_service_register_endpoint(inst0, &ept0, &ept0_cfg);

   /* Wait for endpoint bound (bound_cb called) */
   void *data;
   unsigned char message[] = "hello world";
   uint32_t len = sizeof(message);

   ret = ipc_service_get_tx_buffer(&ept0, &data, &len, K_FOREVER);

   memcpy(data, message, len);

   ret = ipc_service_send_nocopy(&ept0, data, sizeof(message));
}
```

接收示例先用`ipc_service_hold_rx_buffer()`保留接收缓冲区，直接处理或把缓冲区交给其他位置处理，再用`ipc_service_release_rx_buffer()`释放。发送示例调用`ipc_service_get_tx_buffer()`取得发送缓冲区；`K_FOREVER`表示一直等待。随后通过`memcpy()`写入消息，并调用`ipc_service_send_nocopy()`发送。

**原代码译注：**此块定义了`recv_cb_nocopy`，但配置中的`.received`仍写为`recv_cb`。这里保留原代码并指出名称不一致，不能把它当作完整可直接编译的独立示例。原注释还要求等待绑定后再发送；取得缓冲区后的那次`memcpy()`也确实存在于原例，“无拷贝”并不表示这段示例完全没有任何内存复制。

## 92.4\_后端必须与可选支持的能力

后端要求为IPC服务提供灵活性，允许针对具体场景只实现所需功能子集。

| 能力 | 要求 |
| --- | --- |
| 初始化时创建实例 | 必须支持 |
| 运行时在实例上注册端点 | 必须支持 |
| 运行时从实例注销端点 | 可选 |
| 运行时关闭实例 | 可选 |
| 无拷贝API | 可选 |

各后端可以有不同限制与特性。IPC服务API能够同时配合多个后端使用，结合各后端的长处与局限。

原页列出的后端为[ICMsg](P093_ICMsg消息后端.md)及[使用动态分配缓冲区的ICBMsg](P094_ICBMsg块消息后端.md)。

## 92.5\_接口参考

- [IPC服务API](P111_IPC服务公共接口.md)。
- [IPC服务后端API](P115_IPC服务后端接口.md)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：处理器间通信服务目录](P085_处理器间通信服务目录.md) · [本模块主线目录](../reading/intercore_reference.md) · [全部主线](../reading/README.md) · [下一篇：ICMsg消息后端](P093_ICMsg消息后端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：RenesasLinux与Zephyr通信示例](P091_RenesasLinux与Zephyr通信示例.md) · [下一章：ICMsg消息后端](P093_ICMsg消息后端.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
