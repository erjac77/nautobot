from nautobot.core.apps import (
    NavContext,
    NavGrouping,
    NavItem,
    NavMenuAddButton,
    NavMenuGroup,
    NavMenuItem,
    NavMenuTab,
)


menu_items = (
    NavMenuTab(
        name="Virtualization",
        weight=400,
        groups=(
            NavMenuGroup(
                name="Virtual Machines",
                weight=100,
                items=(
                    NavMenuItem(
                        link="virtualization:virtualmachine_list",
                        name="Virtual Machines",
                        weight=100,
                        permissions=[
                            "virtualization.view_virtualmachine",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="virtualization:virtualmachine_add",
                                permissions=[
                                    "virtualization.add_virtualmachine",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="virtualization:vminterface_list",
                        name="Interfaces",
                        weight=200,
                        permissions=[
                            "virtualization.view_vminterface",
                        ],
                        buttons=(),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Clusters",
                weight=200,
                items=(
                    NavMenuItem(
                        link="virtualization:cluster_list",
                        name="Clusters",
                        weight=100,
                        permissions=[
                            "virtualization.view_cluster",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="virtualization:cluster_add",
                                permissions=[
                                    "virtualization.add_cluster",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="virtualization:clustertype_list",
                        name="Cluster Types",
                        weight=200,
                        permissions=[
                            "virtualization.view_clustertype",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="virtualization:clustertype_add",
                                permissions=[
                                    "virtualization.add_clustertype",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="virtualization:clustergroup_list",
                        name="Cluster Groups",
                        weight=300,
                        permissions=[
                            "virtualization.view_clustergroup",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="virtualization:clustergroup_add",
                                permissions=[
                                    "virtualization.add_clustergroup",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)


navigation = (
    NavContext(
        name="Inventory",
        groups=(
            NavGrouping(
                name="Virtualization",
                weight=600,
                items=(
                    NavItem(
                        name="Virtual Machines",
                        weight=100,
                        link="virtualization:virtualmachine_list",
                        permissions=["virtualization.view_virtualmachine"],
                    ),
                    NavItem(
                        name="VM Interfaces",
                        weight=200,
                        link="virtualization:vminterface_list",
                        permissions=["virtualization.view_vminterface"],
                    ),
                    NavItem(
                        name="Clusters",
                        weight=300,
                        link="virtualization:cluster_list",
                        permissions=["virtualization.view_cluster"],
                    ),
                    NavItem(
                        name="Cluster Types",
                        weight=400,
                        link="virtualization:clustertype_list",
                        permissions=["virtualization.view_clustertype"],
                    ),
                    NavItem(
                        name="Cluster Groups",
                        weight=500,
                        link="virtualization:clustergroup_list",
                        permissions=["virtualization.view_clustergroup"],
                    ),
                ),
            ),
        ),
    ),
)
