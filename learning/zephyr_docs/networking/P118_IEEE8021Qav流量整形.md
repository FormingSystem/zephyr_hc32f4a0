---
id: learning.zephyr-docs.networking.page-118
title: IEEE8021Qav流量整形
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/8021Qav.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_IEEE8021Qav流量整形

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/8021Qav.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

基于信用值的整形（Credit-based Shaping）是一种网络调度算法，用于在共享有限网络资源时实现公平性。Zephyr 支持配置 [IEEE 802.1Qav-2009 标准](https://standards.ieee.org/standard/802_1Qav-2009.html)所描述的整形器（Shaper）。Zephyr 本身不实现实际的整形器，只提供配置以太网设备驱动所实现整形器的途径。

## 2. 启用 802.1Qav（Enabling 802.1Qav）

要启用 802.1Qav 整形，以太网设备驱动必须声明支持基于信用值的整形。为此，驱动的能力查询函数返回值必须包含 `ETHERNET_QAV`，通常还需支持优先级队列（Priority Queues），即 `ETHERNET_PRIORITY_QUEUES`：

```c
static enum ethernet_hw_caps eth_get_capabilities(const struct device *dev)
{
        ARG_UNUSED(dev);

        return ETHERNET_QAV | ETHERNET_PRIORITY_QUEUES |
               ETHERNET_HW_VLAN | ETHERNET_LINK_10BASE |
               ETHERNET_LINK_100BASE;
}
```

示例实现可参阅 `sam-e70-xplained` 板的以太网驱动 [`drivers/ethernet/eth_sam_gmac.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_sam_gmac.c)。

## 3. 配置 802.1Qav（Configuring 802.1Qav）

应用可以如下配置基于信用值的整形器：

```c
#include <zephyr/net/net_if.h>
#include <zephyr/net/ethernet.h>
#include <zephyr/net/ethernet_mgmt.h>

static void qav_set_status(struct net_if *iface,
                           int queue_id, bool enable)
{
        struct ethernet_req_params params;
        int ret;

        memset(&params, 0, sizeof(params));

        params.qav_param.queue_id = queue_id;
        params.qav_param.enabled = enable;
        params.qav_param.type = ETHERNET_QAV_PARAM_TYPE_STATUS;

        /* Disable or enable Qav for a queue */
        ret = net_mgmt(NET_REQUEST_ETHERNET_SET_QAV_PARAM,
                       iface, &params,
                       sizeof(struct ethernet_req_params));
        if (ret) {
                LOG_ERR("Cannot %s Qav for queue %d for interface %p",
                        enable ? "enable" : "disable",
                        queue_id, iface);
        }
}

static void qav_set_bandwidth_and_slope(struct net_if *iface,
                                        int queue_id,
                                        unsigned int bandwidth,
                                        unsigned int idle_slope)
{
        struct ethernet_req_params params;
        int ret;

        memset(&params, 0, sizeof(params));

        params.qav_param.queue_id = queue_id;
        params.qav_param.delta_bandwidth = bandwidth;
        params.qav_param.type = ETHERNET_QAV_PARAM_TYPE_DELTA_BANDWIDTH;

        ret = net_mgmt(NET_REQUEST_ETHERNET_SET_QAV_PARAM,
                       iface, &params,
                       sizeof(struct ethernet_req_params));
        if (ret) {
                LOG_ERR("Cannot set Qav delta bandwidth %u for "
                        "queue %d for interface %p",
                        bandwidth, queue_id, iface);
        }

        params.qav_param.idle_slope = idle_slope;
        params.qav_param.type = ETHERNET_QAV_PARAM_TYPE_IDLE_SLOPE;

        ret = net_mgmt(NET_REQUEST_ETHERNET_SET_QAV_PARAM,
                       iface, &params,
                       sizeof(struct ethernet_req_params));
        if (ret) {
                LOG_ERR("Cannot set Qav idle slope %u for "
                        "queue %d for interface %p",
                        idle_slope, queue_id, iface);
        }
}
```

> 译注——片段说明：`qav_set_status()` 通过网络管理请求启用或禁用指定队列的 Qav 功能，代码中的英文注释即此含义。`qav_set_bandwidth_and_slope()` 依次设置带宽参数和空闲斜率（Idle Slope）；每次请求失败时记录对应错误。这是接口用法片段，需要已有的网络接口、有效队列编号和驱动支持，不能单凭返回能力位认定硬件已经完成配置。


<a id="ieee-802-1qav"></a>
<a id="qav"></a>
<a id="overview"></a>
<a id="enabling-802-1qav"></a>
<a id="configuring-802-1qav"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：gPTP通用精确时间协议](P117_gPTP通用精确时间协议.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：流量分类](P119_流量分类.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P117_gPTP通用精确时间协议.md) · [返回大纲](大纲.md) · [下一章](P119_流量分类.md)

</details>

<!-- reading-navigation:end -->
