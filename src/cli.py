import argparse

from topic_modeling.modeling import topic_modeling


def run_cli():
    """
    Function that takes our args from cli and executes the correct app.
    """

    # Adding arg parser
    parser = argparse.ArgumentParser(description="Run different project tools")
    # adding subparser for choosing tool
    subparsers = parser.add_subparsers(dest="tool", description={"Which tool to use"})

    # keyword extraction: add later

    # topic modeling args!
    topic_parser = subparsers.add_parser("topic", help="Run Topic Modeling")

    topic_parser.add_argument(
        "--input",
        type=str,
        default="",
        required=True,
        help="Path to directory of files to be read into tool",
    )

    topic_parser.add_argument(
        "--output",
        type=str,
        default="",
        required=True,
        help="Path to directory for destination of results.",
    )

    topic_parser.add_argument(
        "--name",
        type=str,
        default="",
        required=True,
        help="Name of the run, used in naming the results file",
    )

    topic_parser.add_argument(
        "--uri",
        type=str,
        default="",
        help="URI needed for Neo4j DB",
    )

    topic_parser.add_argument(
        "--auth_username",
        type=str,
        default="",
        help="Neo4j auth username, needed for connection",
    )

    topic_parser.add_argument(
        "--auth_password",
        type=str,
        default="",
        help="Neo4j auth password, needed for connection",
    )

    args = parser.parse_args()

    # choosing which tool to run
    if args.tool == "topic":
        topic_modeling(
            input=args.input,
            output=args.output,
            name=args.name,
            uri=args.uri,
            auth_username=args.auth_username,
            auth_password=args.auth_password,
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    run_cli()
