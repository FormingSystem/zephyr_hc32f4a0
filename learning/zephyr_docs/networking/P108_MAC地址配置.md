---
id: learning.zephyr-docs.networking.page-108
title: MAC地址配置
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/mac_config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_MAC地址配置

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/mac_config.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. MAC 地址配置（MAC Address Configuration）

以太网驱动可以把初始化期间的大部分 MAC 地址处理交给 [`net_eth_mac_config`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mac__config.html) 和 [`net_eth_mac_load()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0)。该结构通常存放在驱动配置中，并使用 [`NET_ETH_MAC_DT_CONFIG_INIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga59882ff8ad5a11c20c08f296edad367e) 或 [`NET_ETH_MAC_DT_INST_CONFIG_INIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac1bb10b6bcc64911128814b9b9de1926) 初始化。这两个宏把设备树（Devicetree）属性转换成以下行为之一：

| 配置类型 | 行为 |
| --- | --- |
| [`NET_ETH_MAC_STATIC`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a9e0096f69300cf30c1f78c33074c1bda) | 使用 `local-mac-address` 属性提供的完整地址。 |
| [`NET_ETH_MAC_RANDOM`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a3fad5d3a2578e83da31f3188add46b87) | 生成随机的本地管理 MAC 地址（Locally Administered MAC Address）；可选地使用 `zephyr,mac-address-prefix` 提供前面的若干字节。 |
| [`NET_ETH_MAC_NVMEM`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a730e86dd6e257352afb233fdcc189955) | 从名为 `"mac-address"` 的非易失存储单元（NVMEM Cell）读取剩余字节；也可以通过 `zephyr,mac-address-prefix` 提供前缀。 |
| [`NET_ETH_MAC_DEFAULT`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a8b1eb5edcd9f4953d56c9c10088d6bb5) | 回退到驱动默认逻辑，例如读取外设寄存器中出厂写入的 MAC 地址。 |

## 2. 驱动集成（Driver Integration）

把 [`net_eth_mac_config`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mac__config.html) 结构嵌入驱动配置，并在驱动数据中放置一个静态缓冲区：

```c
struct my_eth_config {
    struct net_eth_mac_config mac_cfg;
    /* more config fields */
};

struct my_eth_data {
    uint8_t mac_addr[NET_ETH_ADDR_LEN];
    /* more data fields */
};

static const struct my_eth_config my_eth_config_0 = {
    .mac_cfg = NET_ETH_MAC_DT_INST_CONFIG_INIT(0),
};
static struct my_eth_data my_eth_data_0;
```

初始化时，在把地址登记到网络接口之前调用 [`net_eth_mac_load()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0)。这个辅助函数复制静态提供的字节、填充剩余字节，并进行必要的校验。没有提供配置时，驱动仍可回退到片上系统（System on Chip，SoC）专用的存储位置：

```c
static int my_eth_init(const struct device *dev)
{
    const struct my_eth_config *cfg = dev->config;
    struct my_eth_data *data = dev->data;
    int ret;

    ret = net_eth_mac_load(&cfg->mac_cfg, data->mac_addr);
    if (ret == -ENODATA) {
        ret = my_eth_hw_read_mac(dev, data->mac_addr);
    }

    return ret;
}

static void my_eth_iface_init(struct net_if *iface)
{
    const struct device *dev = net_if_get_device(iface);
    struct my_eth_data *data = dev->data;

    net_if_set_link_addr(iface, data->mac_addr, sizeof(data->mac_addr), NET_LINK_ETHERNET);
}
```

> 译注——源码跟踪：以上是驱动集成片段。`my_eth_hw_read_mac()` 代表驱动自行实现的硬件读取逻辑；示例只在返回 `-ENODATA` 时进入该分支，不能把其他错误也当作“没有配置”。MAC 地址缓冲区属于驱动数据，其内容在网络接口登记后仍需有效。辅助函数的实际处理见官方 [`include/zephyr/net/ethernet.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ethernet.h) 中的 `net_eth_mac_load()`；“必要的校验”不应被扩展理解为对所有硬件地址约束都作了检查。

## 3. 设备树示例（Devicetree Examples）

下面的配置片段演示如何为 `&eth0` 这样的以太网控制器节点选择 MAC 地址来源。

### 3.1 静态 MAC 地址（Static MAC Address）

```devicetree
&eth0 {
    local-mac-address = [00 11 22 33 44 55];
};
```

### 3.2 带前缀的随机 MAC 地址（Random MAC Address with Prefix）

```devicetree
&eth0 {
    zephyr,mac-address-prefix = [00 04 25];
    zephyr,random-mac-address;
};
```

> 译注——源码跟踪：随机分支填充剩余字节后，还会清除首字节的组地址位（I/G），并设置本地管理位（U/L）。因此，上例前缀首字节 `00` 最终变为 `02`，不能把所填前缀理解成完全不变的字节序列。

### 3.3 带前缀、来自 NVMEM 的 MAC 地址（NVMEM-provided MAC Address with Prefix）

通过非易失存储器 API（NVMEM API），可以从非易失存储器中取得 MAC 地址；这种存储器通常是电可擦可编程只读存储器（EEPROM）。

```devicetree
&eth0 {
    zephyr,mac-address-prefix = [00 12 34];
    nvmem-cells = <&macaddr_cell>;
    nvmem-cell-names = "mac-address";
};

&eeprom0 {
    nvmem-layout {
        compatible = "fixed-layout";
        #address-cells = <1>;
        #size-cells = <1>;

        macaddr_cell: cell@0 {
            reg = <0x0 0x6>;
            #nvmem-cell-cells = <0>;
        };
    };
};
```

> 译注——源码跟踪：上述 [`net_eth_mac_load()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0) 实现从该 NVMEM 单元的偏移 `0` 读取剩余字节，再放到前缀之后。如果配置了 3 字节前缀，就读取单元开头的 3 字节；并不是自动跳过一个完整 6 字节 MAC 地址的前 3 字节。应按这一读取方式安排存储内容。

如果设备树没有任何 MAC 相关属性，[`net_eth_mac_load()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0) 返回 `-ENODATA`，驱动应使用原有机制，例如读取硬件寄存器或使用构建时常量。

## 4. 运行时修改 MAC 地址（Changing the MAC Address at Runtime）

需要动态设置 MAC 地址的应用，例如要采用管理接口取得的地址，应通过 [`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT) 启用网络管理 API，并使用 [`net_mgmt`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga40e0f9fc86812ad9f6fe174b4c3804e6) 发出 `NET_REQUEST_ETHERNET_SET_MAC_ADDRESS` 请求。

该请求内部调用驱动的 `ethernet_api.set_config()` 实现：

```c
static int app_set_mac_address(const struct device *dev)
{
    struct net_if *iface = net_if_lookup_by_dev(dev);
    struct ethernet_req_params params = {
        .mac_address = { { 0x02, 0x00, 0x5E, 0x01, 0x02, 0x03 } },
    };

    /* Make sure the iface is down */

    return net_mgmt(NET_REQUEST_ETHERNET_SET_MAC_ADDRESS, iface,
                    &params, sizeof(params));
}
```

> 译注——源码跟踪：原示例中的注释要求先让接口关闭，但代码片段本身没有执行关闭操作。调用者必须取得有效接口，并使接口处于管理关闭状态（Administratively Down）。官方 [`subsys/net/l2/ethernet/ethernet_mgmt.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/ethernet_mgmt.c) 在接口仍处于管理启用状态时返回 `-EACCES`；缺少所需驱动配置接口时返回 `-ENOTSUP`。驱动配置成功后才更新网络接口的链路层地址；该请求不会自动关闭接口。


<a id="mac-address-configuration"></a>
<a id="mac-address-config"></a>
<a id="driver-integration"></a>
<a id="devicetree-examples"></a>
<a id="static-mac-address"></a>
<a id="random-mac-address-with-prefix"></a>
<a id="nvmem-provided-mac-address-with-prefix"></a>
<a id="changing-the-mac-address-at-runtime"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：以太网管理](P107_以太网管理.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：链路层地址处理](P109_链路层地址处理.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P107_以太网管理.md) · [返回大纲](大纲.md) · [下一章](P109_链路层地址处理.md)

</details>

<!-- reading-navigation:end -->
