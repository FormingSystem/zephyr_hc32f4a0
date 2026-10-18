---
id: learning.zephyr-docs.networking.page-179
title: OCPP充电桩协议
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ocpp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第179章\_OCPP充电桩协议

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ocpp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

开放充电桩协议（Open Charge Point Protocol，OCPP）是用于充电桩（Charge Point，CP，即电动汽车 EV 充电站）与中央管理系统（Central Management System）之间通信的应用协议。这类中央系统也称充电站网络。OCPP 是开放充电联盟（Open Charge Alliance）定义的[标准](https://openchargealliance.org/protocols/open-charge-point-protocol/)，目标是提供统一的 CP 与中央系统通信方式，使不同厂商的充电桩和中央系统能够互联。

Zephyr 提供基于 WebSocket API、使用 JSON 载荷的 OCPP CP 库，通过 [`CONFIG_OCPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OCPP) 启用。本页当前支持范围为 OCPP 1.6 的基本核心功能集（Core Profile）。

CP 需要连接中央系统（Central System，CS）服务器。开发时可在本地搭建开源 SteVe 服务器，安装方法见[SteVe 服务器说明](https://github.com/steve-community/steve/blob/master/README.md)。

Zephyr OCPP CP 库实现：

- 处理套接字连通性及事件的引擎。
- OCPP 核心功能，包括载荷组帧／解析、向用户通知 OCPP 事件和心跳（Heartbeat）通知。

## 2. 示例用法（Sample Usage）

### 2.1 初始化库

用完整的 CP 和 CS 信息初始化 OCPP 库。初始化前，以太网、Wi-Fi 或调制解调器（Modem）网络接口应已经就绪。向 `ocpp_init` 传入填好的 CP、CS 结构体以及用户回调。

```c
static int user_notify_cb(ocpp_notify_reason_t reason,
                          ocpp_io_value_t *io,
                          void *user_data)
{

     switch (reason) {
     case OCPP_USR_GET_METER_VALUE:
             ...
             break;

     case OCPP_USR_START_CHARGING:
             ...
             break;

             ...
             ...
}

/* OCPP configuration */
ocpp_cp_info_t cpi = { "basic", "zephyr", .num_of_con = 1};
ocpp_cs_info_t csi =  {"192.168.1.3",   /* ip address */
                       "/steve/websocket/CentralSystemService/zephyr",
                       8180,
                       AF_INET};

ret = ocpp_init(&cpi, &csi, user_notify_cb, NULL);
```

> 译注：原片段含省略号，不是可独立编译的完整 C 程序；回调中的省略分支和返回值需要应用实现。原文的 `ocpp_notify_reason_t`、`ocpp_io_value_t`、`ocpp_cp_info_t`、`ocpp_cs_info_t` 属于旧示例写法，当前官方[ocpp.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ocpp.h)分别使用 `enum ocpp_notify_reason`、`union ocpp_io_value`、`struct ocpp_cp_info`、`struct ocpp_cs_info`。原示例保留不静默改写，编写当前版本应用时按头文件定义及[完整示例](P182_OCPP充电桩示例.md)使用。

示例中的 `192.168.1.3`、端口 `8180` 和 WebSocket URL 路径属于服务器配置，需要替换成自己的开发服务器；URL 路径不是本地文件系统地址。

### 2.2 为每个连接器打开会话

调用任意 OCPP 事务 API 前，必须为每个物理连接器（Physical Connector）打开独立会话（Session）：

```c
ocpp_session_handle_t sh = NULL;
ret = ocpp_session_open(&sh);
```

### 2.3 授权（Authorization）

`idtag` 是电动汽车用户的认证令牌，应与 CS 保存的列表匹配。如果充电请求由本地 CP 发起，在向车辆传输能量前，必须发送授权请求，确认该令牌有效：

```c
ocpp_auth_status_t status;
ret = ocpp_authorize(sh, idtag, &status, 500);
```

调用成功后，授权结果位于 `status`。

> 源码说明：当前状态类型为 `enum ocpp_auth_status`。`ocpp_authorize()` 返回 `0` 表示调用成功，还必须检查结果是否为 `OCPP_AUTH_ACCEPTED`，不能只凭返回值启动充电。参数 `500` 的单位是毫秒，见[接口定义](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ocpp.h)。

### 2.4 开始事务（Start Transaction）

充电请求也可以来自 CS，此时通过 `OCPP_USR_START_CHARGING` 回调通知应用；原文称该路径中再次调用授权请求是可选的。原文随后写道，当 CS 准备向 EV 供电时，使用 `ocpp_start_transaction` 向 CS 通知事务开始，附上电表读数和连接器编号：

```c
const int idcon = 1;
const int mval = 25; //meter reading in wh
ret = ocpp_start_transaction(sh, mval, idcon, 200);
```

> 译注：原文这里把“准备供电”的主体写成 CS；实际能源输出位于充电桩 CP 侧，CS 是管理与通信对端，不能把协议事务通知等同于中央服务器直接供电。示例的 `mval=25` 是瓦时（Watt-hour，Wh）能量读数，不是瞬时功率；`idcon=1` 是连接器编号，接口要求其大于零并连续编号；最后的 `200` 是毫秒超时。

事务成功开始后，库调用用户回调获取电表读数。回调不应长时间阻塞，以免阻塞协议栈／库的处理。

## 3. API 参考与相关示例

完整接口入口：[OCPP 库 API](P191_OCPP完整API参考.md)。

[OCPP 充电桩示例](P182_OCPP充电桩示例.md#ocpp)连接中央系统并模拟电表读数。它属于协议示例，不是已经验证的电动汽车功率控制实现。


<a id="open-charge-point-protocol-ocpp"></a>
<a id="ocpp-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="overview"></a>
<a id="sample-usage"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：MCP服务器](P178_MCP服务器.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P178_MCP服务器.md) · [返回大纲](大纲.md) · [下一章](P180_MCP示例目录.md)

</details>

<!-- reading-navigation:end -->
