from loguru import logger

Amount = 200


class Coordinator:
    def __init__(self) -> None:
        self.workers = []
        self.votes = []
        self.acks = []

    def yes(self):
        self.votes.append(True)
        logger.debug("Add yes")

    def no(self):
        self.votes.append(False)
        logger.debug("Add no")

    def ack(self):
        self.acks.append(True)
        logger.debug("Add acks")

    def start_voting(self, worker):
        self.workers.append(worker)
        logger.debug("Start voting")

    def run(self):
        for worker in self.workers:
            logger.debug("Query to commit")
            worker.query_to_commit()
        if all(self.votes):
            logger.debug("Commit")
            for worker in self.workers:
                worker.commit()
        else:
            logger.debug(self.votes)
            for worker in self.workers:
                worker.rollback()
        if all(self.acks):
            pass
        else:
            pass
        for worker in self.workers:
            logger.debug(f"Finish {worker.name}")
            worker.finish()


class Worker:
    def __init__(self, name, coord) -> None:
        self.name = name
        self.coord = coord
        self.do = None
        self.undo = None
        self.ready = None

    def query_to_commit(self):
        if self.ready is True:
            logger.debug("Vote Yes")
            self.coord.yes()
        elif self.ready is False:
            logger.debug("Vote No")
            self.coord.no()

    def commit(self):
        logger.debug("commit")
        self.commit = True

    def rollback(self):
        logger.debug("rollback")
        self.commit = False

    def run(self):
        self.ready = Amount >= 0
        logger.debug(Amount)
        self.coord.start_voting(self)

        if self.commit:
            logger.debug("Commit!!")
        else:
            for undo in self.undo:
                undo()
            logger.debug("Rollback!!")

        self.coord.ack()

    def finish(self):
        logger.debug("Finish")


if __name__ == "__main__":
    coordinator = Coordinator()
    fly_booking = Worker("Fly", coordinator)
    hotel_booking = Worker("Hotel", coordinator)
    account = Worker("Account", coordinator)

    fly_booking.client_name = "Nik"
    fly_booking.fly_number = "KLM 1382"
