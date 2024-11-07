import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.step_mission_compensation import StepMissionCompensationData
from lib.proto import (
    GetChallengeStepCompensationInfoReq,
    GetChallengeStepCompensationInfoRsp,
    ChallengeStepCompensation,
    StepCompensation
)

async def handle(session: Session, msg: GetChallengeStepCompensationInfoReq) -> betterproto.Message:
    return GetChallengeStepCompensationInfoRsp(
        retcode=0,
        compensation_list=[
            ChallengeStepCompensation(
                compensation_id=challenge.CompensationID,
                is_take_compensation=True,
                new_challenge_step_compensation_list=[
                    StepCompensation(
                        step_id=id
                    ) for id in challenge.NewChallengeStepIDList
                ],
                old_challenge_step_compensation_list=[
                    StepCompensation(
                        step_id=id
                    ) for id in challenge.OldChallengeStepIDList
                ],
                mainline_step_compensation_list=[
                    StepCompensation(
                        step_id=id
                    ) for id in challenge.MainLineStepIDList
                ]
            )
            for challenge in ResourceManager.instance().values(StepMissionCompensationData)
        ]
    )
