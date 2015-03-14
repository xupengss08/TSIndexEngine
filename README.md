# TSIndexEngine
An engine for search short time-series from a large number of time-series data based on shape similarity.

项目中包含了如下5个包：
1）model：模型相关的数据结构
2）preprocess：预处理阶段的代码文件，其中entry.py是其入口文件，可以直接运行，该阶段主要读取设备工况数据，
进行解析处理，最终生成处理完成后的切片文件
3）slicecluster:聚类相关的代码文件，entry.py为入口文件，其中有分桶和聚类的相关方法，我只是简单实现了，
还没有完成处理好
4）util：工具类
5）resources：相关数据的文件夹，其中raw_data文件夹存放各设备的工况数据；aligned_slice文件夹存放预处理
后的文件，这里我只有一个文件result.dt；cluster文件夹存放聚类结果文件，其中bucket.mapping为分桶结果文件，
其他.idx文件是聚类后生成的索引文件。

(既然所有的切片都服从一种分布，那我们为何不将分布挑出来，拿模式上的扰动来提取特征，再去聚类检索呢）
