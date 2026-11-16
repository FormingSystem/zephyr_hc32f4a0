---
id: computer-architecture-017-model
title: DMA缓冲所有权与缓存交接
kind: tutorial
status: maintained
domains: [computer-architecture, embedded]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_DMA缓冲所有权与缓存交接

> [P01 总目录](../大纲.md) / [P017 DMA缓存与总线竞争](大纲.md) / 第 1 篇（共 3 篇）


CPU 与 DMA 都能访问某块 RAM，并不意味着它们此刻看到相同数据。缓存可能保存 CPU 的副本，DMA 则沿自己的路径访问内存。本专题用显示发送缓冲解释所有权，再把方向反转到接收。

```mermaid
%%{init: {"markdownAutoWrap": false, "flowchart": {"wrappingWidth": 280}, "themeVariables": {"fontSize": "16px"}}}%%
flowchart TB
 subgraph CPUOWN["阶段一<br/>CPU拥有发送缓冲"]
  FILL["CPU生成像素"] --> CACHE["D-cache<br/>已修改的缓存行"]
  CACHE -->|"clean：写回修改"| RAM["DMA可达的RAM<br/>发送缓冲区"]
 end
 RAM --> ORDER["按平台规则<br/>完成维护与同步"]
 ORDER --> START["配置并启动DMA"]
 subgraph DMAOWN["阶段二<br/>DMA读取<br/>CPU不再修改"]
  START --> READ["DMA从RAM读取像素"]
  READ --> DEVICE["交给显示接口"]
  DEVICE --> DONE["核对DMA完成<br/>及所需外设条件"]
 end
 DONE -->|"归还缓冲所有权"| FILL
 classDef control fill:#f3e8ff,stroke:#9333ea,color:#172b4d
 classDef storage fill:#fff7ed,stroke:#c2410c,color:#172b4d
 classDef default fill:#eff6ff,stroke:#2563eb,color:#172b4d
 class ORDER,START,DONE control
 class CACHE,RAM storage
```

图例：**蓝色节点表示一般参与者，紫色突出处理或决策，橙色表示保存的数据或状态。** 实线是数据或所有权交接顺序；两个阶段共享同一缓冲，不是复制出两份应用数组。`D-cache(Data Cache-数据缓存)：保留 CPU 数据访问的缓存副本。` clean 将需要写回的修改送向内存；invalidate 丢弃缓存副本，使后续读取重新获得内存内容。

发送方向是 CPU 写、DMA 读。如果 CPU 只改了缓存，RAM 仍可能保留旧像素。正确交接需要让 DMA 可见的数据先到达内存，再发布启动动作；启动后 CPU 不能在 DMA 尚未读取完时修改同一缓冲，否则一帧可能混入两个版本。单独执行缓存维护不能代替所有权纪律。

接收方向是 DMA 写、CPU 读。DMA 完成后，CPU 还可能读到旧缓存，所以需要按接收协议失效相关缓存行。接收前也必须处理可能存在的脏行，防止它们稍后写回覆盖 DMA 新数据；开始前、完成后各自的维护与同步需按平台要求安排。不能只记住“DMA之后invalidate”这一句口号。

M7 数据缓存行按32字节组织。维护 API 的范围扩展可能涉及缓冲两侧同一行的邻居；如果邻居保存别的重要脏数据，失效可能破坏它。**对齐缓冲首地址还不够，分配长度与相邻对象也要隔离。** 不可缓存区域可以简化一致性，却仍需可达性、顺序与所有权保证。

<a id="section-1"></a>

## 1.1\_缓存维护之前先约定谁可以碰缓冲

发送缓冲经过三个责任阶段：CPU 可写、交给 DMA、DMA 完成后可重用。CPU 可写阶段允许生成内容；发布 DMA 启动之前，按平台要求处理缓存和同步；DMA 拥有阶段，CPU 不得修改它尚未读取完的字节。即使每次修改都立即 clean，也不能保证 DMA 读到同一版本的整帧。

举例：DMA 已读完前半幅图，CPU 此时覆盖整个缓冲并写回缓存，DMA 随后读到后半幅新图。所有字节都可能来自有效内存，显示结果仍是混合帧。这个错误属于所有权交接，而不是“缓存没有刷新干净”。双缓冲的意义正是让 CPU 与 DMA 在不同对象上工作，并在明确完成点交换角色。

接收方向同理。DMA 正在写入期间 CPU 不应读取半成品；完成后还需按缓存协议取得新数据。完成通知只证明控制器声明的那件事完成，队列中的缓冲引用还要指向没有被下一轮接收重新占用的对象。要把“搬完”“可读”“可以归还”分别定义，才能组合连续采样与异步处理。

---

[← 嵌套异常的栈地址推演](../P016_exception_context/P003_嵌套异常的栈地址推演.md) · [本专题目录](大纲.md) · [可达性缓存维护与缓存行边界 →](P002_可达性缓存维护与缓存行边界.md)
