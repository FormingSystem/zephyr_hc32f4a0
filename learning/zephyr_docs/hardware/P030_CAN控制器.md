---
id: learning.zephyr-docs.hardware.periph-can-controller
title: CAN控制器
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/can/controller.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第30章\_CAN控制器

原文：[CAN Controller](https://docs.zephyrproject.org/latest/hardware/peripherals/can/controller.html)。读取日期：2026-10-13，`latest`。

## 30.1\_CAN控制器与初始化

**控制器局域网（Controller Area Network，CAN）**是双线串行总线，原文引用Bosch CAN规范、Bosch可变数据速率CAN规范，以及ISO 11898-1:2003。ISO为 **国际标准化组织（International Organization for Standardization）**。CAN以汽车应用著称，也用于家庭和工业自动化等产品。

**原文警告：**控制器只有在总线至少连续11个隐性位时间保持空闲时才能初始化。因此CAN接收线CAN RX必须至少短暂保持高电平；即使 **回环模式（Loopback Mode）**也需要这个条件。

## 30.2\_位时序与采样点

下图保留原文根据ISO 11898-1:2003绘制的 **位时序（Bit Timing）**：

![CAN位时间分段官方原图](images/timing.svg)

一个位划分为四段，计数单位为 **时间量子（Time Quantum）**：

| 原图名称 | 中文含义与作用 |
| --- | --- |
| `Sync_Seg` | 同步段（Synchronization Segment），节点在其边沿同步，长度固定为1个时间量子。 |
| `Prop_Seg` | 传播段（Propagation Segment），补偿总线信号传播以及收发器、节点的其他延迟。 |
| `Phase_Seg1` | 相位缓冲段1（Phase Buffer Segment 1），在此段结束处采样。 |
| `Phase_Seg2` | 相位缓冲段2（Phase Buffer Segment 2），与前一段共同确定采样位置。 |

位时间等于四段的量子数之和乘单个量子时长；**位率（Bitrate）**是位时间的倒数。**采样点（Sample Point）**位于Phase_Seg1和Phase_Seg2之间，是使用者需要选择的参数。原文引述 **CAN自动化协会（CAN in Automation，CiA）**推荐87.5%的采样点。

**重同步跳转宽度（Synchronization Jump Width，SJW）**以时间量子表示需要重同步时采样点最多可移动的量。初始时序从设备树取得，可按SJW、位率、采样点设置，也可按位率及传播段、两个相位段设置，并可经运行时时序接口修改。

> 译注：87.5%是原文给出的建议值，不是所有位率、总线长度、控制器和 **可变数据速率CAN（CAN with Flexible Data-Rate，CAN FD）**数据阶段都通用的固定配置。

## 30.3\_标识符、仲裁与过滤

CAN通过 **标识符（Identifier）**识别帧，而不是通过节点地址寻址。**标准帧（Standard Frame，也称Basic Frame）**使用11位标识符，**扩展帧（Extended Frame）**使用29位；Zephyr接口可同时支持两种。

帧以一个显性 **帧起始位（Start Of Frame）**开始，随后是标识符，进入 **仲裁阶段（Arbitration Phase）**。此阶段允许节点同时发送：显性覆盖隐性，节点监视总线，发现自己的发送被覆盖就退出本次发送。因此低编号标识符获得较高优先级。

**过滤器（Filter）**列出节点关心的标识符，未匹配任何过滤器的帧被忽略。**掩码（Mask）**可以精确或部分匹配：标准标识符的11位或扩展标识符的29位掩码全为1时精确匹配；掩码位为0时忽略对应标识符位。硬件过滤器数量通常有限，Kconfig也限制数量以节省内存。

## 30.4\_错误帧与总线状态

节点检测到错误帧时，通过 **错误帧（Error Frame）**部分覆盖当前传输。根据控制器状态，可发送主动或被动错误帧。处于 **错误主动状态（Error-active）**时发送连续6个显性位，违反位填充规则，因而能被其他节点检测，原发送者可随后重发。

原文列出初始化后节点的三种状态：错误主动、**错误被动（Error-passive）**和 **总线关闭（Bus-off）**。初始化后处于错误主动状态，可发送主动错误帧、**确认（Acknowledgement，ACK）**和过载帧。

每个节点具有接收与发送错误计数器。任一计数器超过127时转入错误被动状态，不再允许发送主动错误帧。原文接着写发送错误计数“增加到255”后进入bus-off，此时不得向总线发送任何显性位；收到128次连续11个隐性位的序列后可以恢复。

> 译注：原文“到255”与本地 `can.h` 中bus-off状态的 `>=256` 注释不一致；理解发送错误计数阈值时不要把255误作256。是否自动恢复还取决于控制器恢复模式，手动恢复见[CAN命令行](P032_CAN命令行.md)。

原文另附[CAN百科入口](https://en.wikipedia.org/wiki/CAN_bus)供延伸阅读。其列出的Zephyr能力为标准/扩展标识符、带掩码过滤、回环和静默模式，以及 **远程请求（Remote Request）**。

## 30.5\_阻塞发送

以下片段使用结构体 `can_frame` 表示帧，函数 `can_send()` 发送它。宏 `DEVICE_DT_GET` 和 `DT_CHOSEN` 从设备树选择 `zephyr_canbus` 设备；时间宏 `K_MSEC()` 表示毫秒超时，`LOG_ERR` 是错误日志宏。

标准标识符 `0x123`、8字节数据的原例：

```c
struct can_frame frame = {
        .flags = 0,
        .id = 0x123,
        .dlc = 8,
        .data = {1,2,3,4,5,6,7,8}
};
const struct device *const can_dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus));
int ret;

ret = can_send(can_dev, &frame, K_MSEC(100), NULL, NULL);
if (ret != 0) {
        LOG_ERR("Sending failed [%d]", ret);
}
```

回调参数为 `NULL` 时，发送函数阻塞，直到帧已发送并由至少另一个节点确认，或发生错误。**超时只约束获取发送邮箱的等待时间**；一旦分配到邮箱，不能用这个超时取消已开始的发送。

> 译注：原代码是功能片段，不含完整的设备就绪检查与控制器启动流程；实际应用需先确认所选设备和控制器可用。字段 `dlc` 是 **数据长度码（Data Length Code，DLC）**，本例经典CAN的值8对应8字节。

## 30.6\_带回调的发送

扩展标识符 `0x1234567`、2字节数据的原例使用标志 `CAN_FRAME_IDE` 选择扩展标识符；发送结束或发生错误时调用 `tx_callback`。常量 [`K_FOREVER`](../timer_reference/P086_系统时钟公共接口.md) 让获取发送邮箱一直等待，但有回调时，函数不等待帧最终发送完成：

```c
void tx_callback(const struct device *dev, int error, void *user_data)
{
        char *sender = (char *)user_data;

        if (error != 0) {
                LOG_ERR("Sending failed [%d]\nSender: %s\n", error, sender);
        }
}

int send_function(const struct device *can_dev)
{
        struct can_frame frame = {
                .flags = CAN_FRAME_IDE,
                .id = 0x1234567,
                .dlc = 2
        };

        frame.data[0] = 1;
        frame.data[1] = 2;

        return can_send(can_dev, &frame, K_FOREVER, tx_callback, "Sender 1");
}
```

回调参数 `error` 表示发送结果，`user_data` 为调用者提供的上下文；本例传入字符串 `Sender 1`。邮箱分配等待与发送完成通知是两个阶段。

## 30.7\_中断回调接收

只有匹配过滤器的帧才被接收。函数 [`can_add_rx_filter()`](P362_CAN控制器接口.md) 添加过滤器时可指定用户数据，接收回调得到帧及该数据：

```c
void rx_callback_function(const struct device *dev, struct can_frame *frame, void *user_data)
{
        ... do something with the frame ...
}
```

原文省略号是待实现的处理逻辑，不能直接编译。通过回调接收最直接高效，但回调在 **中断上下文（Interrupt Context）**执行，必须尽量短且不得阻塞；不能从 **用户空间（Userspace）**添加这种回调。

下面的结构体 `can_filter` 用标准标识符全掩码常量 `CAN_STD_ID_MASK` 精确匹配 `0x123`：

```c
const struct can_filter my_filter = {
        .flags = 0U,
        .id = 0x123,
        .mask = CAN_STD_ID_MASK
};
int filter_id;
const struct device *const can_dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus));

filter_id = can_add_rx_filter(can_dev, rx_callback_function, callback_arg, &my_filter);
if (filter_id < 0) {
  LOG_ERR("Unable to add rx filter [%d]", filter_id);
}
```

返回非负值为过滤器编号，负值表示失败。**译注：**原片段的 `callback_arg` 由应用自行定义；回调中的帧指针不能在未复制数据的情况下被当作无限期有效的应用缓存。

## 30.8\_消息队列接收与移除过滤器

函数 [`can_add_rx_filter_msgq()`](P362_CAN控制器接口.md) 通过 **消息队列（Message Queue）**同步接收，可从用户空间调用。队列容量应能容纳预期积压帧。

原例用标志 `CAN_FILTER_IDE` 选择扩展帧，用常量 `CAN_EXT_ID_MASK` 全匹配 `0x1234567`。宏 `CAN_MSGQ_DEFINE` 定义容量为2的队列，函数 `k_msgq_get()` 从队列取帧，`K_FOREVER` 表示等待：

```c
const struct can_filter my_filter = {
        .flags = CAN_FILTER_IDE,
        .id = 0x1234567,
        .mask = CAN_EXT_ID_MASK
};
CAN_MSGQ_DEFINE(my_can_msgq, 2);
struct can_frame rx_frame;
int filter_id;
const struct device *const can_dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus));

filter_id = can_add_rx_filter_msgq(can_dev, &my_can_msgq, &my_filter);
if (filter_id < 0) {
  LOG_ERR("Unable to add rx msgq [%d]", filter_id);
  return;
}

while (true) {
  k_msgq_get(&my_can_msgq, &rx_frame, K_FOREVER);
  ... do something with the frame ...
}
```

这里的省略号同样代表应用处理逻辑。函数 [`can_remove_rx_filter()`](P362_CAN控制器接口.md) 用先前返回的过滤器编号移除过滤器：

```c
can_remove_rx_filter(can_dev, filter_id);
```

## 30.9\_修改位率与采样点

初始位率与采样点按设备树配置在运行时初始化。函数 [`can_calc_timing()`](P362_CAN控制器接口.md) 根据位率和以千分数表示的采样点计算结构体 `can_timing`；函数 [`can_set_timing()`](P362_CAN控制器接口.md) 应用它。

下面设置250000 bit/s与87.5%采样点，参数875表示875‰。计算函数返回负值为失败，正值表示采样点误差，0表示无误差；信息日志宏 `LOG_INF` 用于显示偏差。先通过 `can_stop()` 停止控制器，设置后再用 `can_start()` 启动：

```c
struct can_timing timing;
const struct device *const can_dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus));
int ret;

ret = can_calc_timing(can_dev, &timing, 250000, 875);
if (ret > 0) {
  LOG_INF("Sample-Point error: %d", ret);
}

if (ret < 0) {
  LOG_ERR("Failed to calc a valid timing");
  return;
}

ret = can_stop(can_dev);
if (ret != 0) {
  LOG_ERR("Failed to stop CAN controller");
}

ret = can_set_timing(can_dev, &timing);
if (ret != 0) {
  LOG_ERR("Failed to set timing");
}

ret = can_start(can_dev);
if (ret != 0) {
  LOG_ERR("Failed to start CAN controller");
}
```

> 译注：原例在停止或配置失败后仅打印日志，仍继续下一步。完整应用应按错误结果决定是否继续，不能把后续启动成功当成此前时序已经正确应用。

支持 **可变数据速率CAN（CAN with Flexible Data-Rate，CAN FD）**的控制器还有数据阶段时序接口：[`can_calc_timing_data()`](P362_CAN控制器接口.md) 与 [`can_set_timing_data()`](P362_CAN控制器接口.md)。

## 30.10\_SocketCAN、示例与接口

SocketCAN将 **伯克利套接字接口（Berkeley Sockets API，BSD Socket API）**的用法带到CAN；BSD来自Berkeley Software Distribution的历史名称。Zephyr实现与Linux SocketCAN兼容，便于使用基于它构建的高层项目。但帧会先路由到网络协议栈，而非直接交给应用，增加计算和内存开销。API表示 **应用程序编程接口（Application Programming Interface）**。

原文列出两个可直接构建的示例：[CAN计数器](P044_CAN计数器示例.md)与[SocketCAN示例](../networking/P206_SocketCAN示例.md#socket-can)。页面的相关示例区还列出[持续发送节点（Babbling Node）](P045_CAN持续发送示例.md)，用于模拟不停发送的CAN节点；计数器示例用于发送和接收消息。

完整参考见[CAN控制器API](P362_CAN控制器接口.md)，测试替身入口为[Fake CAN Controller](P374_伪CAN控制器接口.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CAN总线入口](P029_CAN总线入口.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：CAN收发器](P031_CAN收发器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：CAN总线入口](P029_CAN总线入口.md) · [下一章：CAN收发器](P031_CAN收发器.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
