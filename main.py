import datetime
import matplotlib.pyplot as plt
import random
from map_data import gen_area_data


def sort_node(node_list):  # early to late
    # input list of unsorted nodes and sort them in chronological order

    def swap(i, j):
        node_list[i], node_list[j] = node_list[j], node_list[i]

    n = len(node_list)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if node_list[i - 1].time > node_list[i].time:
                swap(i - 1, i)
                swapped = True

    return node_list


def plot_trail(img_path, data, time_start, time_end, box_range):  # plots trails of vessels within a time range
    im = plt.imread(img_path)

    fig, ax = plt.subplots()

    for vessel_nodes_list in data.values():
        x = []
        y = []
        vessel_path_list = sort_node(vessel_nodes_list)
        for ts in vessel_path_list:
            x.append(ts.pos[1])
            y.append(ts.pos[0])
            color = random.choice(['r', 'g', 'b', 'k', 'y'])
            ax.scatter(x, y, zorder=2, alpha=0.2, c=color, s=10)
            ax.plot(x, y, zorder=1, c=color, linewidth=0.3)
            # plt.text(x, y, 'yes', fontsize=5)

    ax.set_title('New York Bay from time={} to time={}'.format(time_start, time_end))
    ax.set_xlim(box_range[0], box_range[1])
    ax.set_ylim(box_range[2], box_range[3])
    ax.imshow(im, zorder=0, extent=box_range, aspect='equal')
    plt.show()


def main():
    BBox = (-74.35, -73.71, 40.38, 40.66)  # lonmin, lonmax, latmin, latmax

    start_time_input = '2020-01-01T00:00:00'
    end_time_input = '2020-01-01T01:00:00'

    start_time = datetime.datetime.strptime(start_time_input, '%Y-%m-%dT%H:%M:%S')
    end_time = datetime.datetime.strptime(end_time_input, '%Y-%m-%dT%H:%M:%S')

    csv_data = 'ny_bay_AIS_2020_01_01.csv'
    img = 'ny_bay (-74.35, -73.71, 40.38, 40.66).png'

    area_data = gen_area_data(csv_data, BBox, start_time, end_time)
    # pygame for map??
    # graph
    plot_trail(img, area_data, start_time, end_time, BBox)


if __name__ == '__main__':
    main()
