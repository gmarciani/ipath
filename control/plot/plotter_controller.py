#MatPlotLib Import
import matplotlib.pyplot as plt
    
def make_plot(dataset, plot_label, xlabel, ylabel, legend):
    """
    Generates a MatPlotLib plot from the specified dataset and with the specified labeling features.
    
    make_plot(dataset, plot_label, xlabel, ylabel, legend) -> plt
    
    @type dataset: list of list
    @param dataset: formatted dataset.
    @type plot_label: string
    @param plot_label: plot title.
    @type xlabel: string
    @param xlabel: x-axis plot label.
    @type ylabel: string
    @param ylabel: y-axis plot label
    @type legend: tuple
    @param legend: plot legend.
    
    @rtype: MatPlotLib plot
    @return: plot
    """
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])
    plt.title(plot_label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    for data, lbl in zip(dataset, legend): 
        ax.plot(data[0], data[1], label = lbl)
        ax.legend(bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0.) 
    return plt

def make_table(dataset, table_label, xlabel, ylabel, legend):
    """
    Generates a table-as-string from the specified dataset and with the specified labeling features.
    
    make_table(dataset, table_label, xlabel, ylabel, legend) -> s
    
    @type dataset: list of list 
    @param dataset: formatted dataset.
    @type table_label: string
    @param table_label: table title.
    @type xlabel: string
    @param xlabel: x-column table label.
    @type ylabel: string
    @param ylabel: y-column table label.
    @type legend: tuple
    @param legend: table legend.
    
    @rtype: string
    @return: table
    """
    s = ""
    if table_label is not None:
        s += "*{}*\n".format(str("*" * (len(table_label) + 2)))
        s += "* {} *\n".format(str(table_label))
        s += "*{}*\n\n".format(str("*" * (len(table_label) + 2)))
        
    s += "Measure: ({}, {})\n".format(str(xlabel), str(ylabel))
    
    for data, lbl in zip(dataset, legend):
            s += "\n*{}*\n".format(str("*" * (len(lbl) + 2)))
            s += "* {} *\n".format(str(lbl))
            s += "*{}*\n\n".format(str("*" * (len(lbl) + 2)))
            for x, y in zip(data[0], data[1]):
                s += "|\t{}\t|\t{}\n".format(str(x), str(y))
    return s    

def save_plot(plot, path):
    """
    Saves MatPlotLib plot in path.
    
    save_plot(plot, path) -> None
    
    @type plot: MatPlotLib plot
    @param plot: plot.
    @type path: string
    @param path: absolute file path.
    """
    plot.savefig(path)
    
def save_table(table, path):
    """
    Saves table in path.
    
    save_table(table, path) -> None
    
    @type table: string
    @param table: table as string.
    @type path: string
    @param path: absolute file path.
    """
    file_stream = open(path, "w")
    file_stream.write(table)
    file_stream.close()